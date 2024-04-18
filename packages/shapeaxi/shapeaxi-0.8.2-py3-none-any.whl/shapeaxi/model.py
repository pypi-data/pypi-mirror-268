from . import saxi_nets, utils
import scipy.io as sio 
import numpy as np
import glob
import math, multiprocessing, os
import torch
import vtk
abspath = os.path.abspath(os.path.dirname(__file__))

# device = "cuda:1"
# SAXINETS = getattr(saxi_nets, "SaxiIcoClassification_fs_CT_DS")
# model = SAXINETS.load_from_checkpoint('/CMF/data/floda/data_files_CT_DS/train/fold2/epoch=21-val_loss=0.55.ckpt')


class vtkLoopSubdivisionFilter(vtk.vtkPolyDataAlgorithm):
    LoopWeights = [0.375, 0.375, 0.125, 0.125]

    def __init__(self):
        self.NumberOfSubdivisions = 2
        self.CheckAbort = None

    def RequestData(self, request, inInfo, outInfo):
        inputDS = vtk.vtkPolyData.GetData(inInfo[0])
        output = vtk.vtkPolyData.GetData(outInfo)
        edgeData = vtk.vtkIntArray()

        output.Initialize()
        edgeData.SetNumberOfComponents(3)
        edgeData.SetNumberOfTuples(inputDS.GetNumberOfCells())

        self.GenerateSubdivisionPoints(inputDS, edgeData, output.GetPoints(), output.GetPointData())

        output.SetPoints(output.GetPoints())
        output.SetPolys(inputDS.GetPolys())
        output.GetCellData().AddArray(edgeData)

        return 1

    def GenerateSubdivisionPoints(self, inputDS, edgeData, outputPts, outputPD):
        numPts = inputDS.GetNumberOfPoints()
        pts = inputDS.GetPoints()
        inputPD = inputDS.GetPointData()
        inputPolys = inputDS.GetPolys()
        cellIds = vtk.vtkIdList()
        stencil = vtk.vtkIdList()
        edgeTable = vtk.vtkEdgeTable()
        weights = [0.0] * 256
        abort = False

        edgeTable.InitEdgeInsertion(inputDS.GetNumberOfPoints())

        for ptId in range(numPts):
            abort = self.CheckAbort()
            if abort:
                break
            if self.GenerateEvenStencil(ptId, inputDS, stencil, weights):
                self.InterpolatePosition(pts, outputPts, stencil, weights)
                outputPD.InterpolatePoint(inputPD, ptId, stencil, weights)
            else:
                return 0

        cellId = 0
        inputPolys.InitTraversal()
        while not abort and inputPolys.GetNextCell(cellIds):
            p1 = cellIds.GetId(2)
            p2 = cellIds.GetId(0)

            for edgeId in range(3):
                abort = self.CheckAbort()
                if abort:
                    break

                if edgeTable.IsEdge(p1, p2) == -1:
                    edgeTable.InsertEdge(p1, p2)
                    inputDS.GetCellEdgeNeighbors(-1, p1, p2, cellIds)
                    if cellIds.GetNumberOfIds() == 1:
                        stencil.SetNumberOfIds(2)
                        stencil.SetId(0, p1)
                        stencil.SetId(1, p2)
                        weights[0] = 0.5
                        weights[1] = 0.5
                    elif cellIds.GetNumberOfIds() == 2:
                        self.GenerateOddStencil(p1, p2, inputDS, stencil, weights)
                    else:
                        print("Dataset is non-manifold and cannot be subdivided. Edge shared by", cellIds.GetNumberOfIds(), "cells")
                        return 0

                    newId = self.InterpolatePosition(pts, outputPts, stencil, weights)
                    outputPD.InterpolatePoint(inputPD, newId, stencil, weights)
                else:
                    newId = self.FindEdge(inputDS, cellId, p1, p2, edgeData, cellIds)

                edgeData.SetComponent(cellId, edgeId, newId)
                p1 = p2
                if edgeId < 2:
                    p2 = cellIds.GetId(edgeId + 1)

            cellId += 1

        return 1

    def GenerateEvenStencil(self, p1, polys, stencilIds, weights):
        cellIds = vtk.vtkIdList()
        ptIds = vtk.vtkIdList()
        cell = vtk.vtkCell()
        p = p2 = bp1 = bp2 = startCell = nextCell = 0
        numCellsInLoop = 0

        polys.GetPointCells(p1, cellIds)
        numCellsInLoop = cellIds.GetNumberOfIds()

        if numCellsInLoop < 1:
            print("numCellsInLoop < 1:", numCellsInLoop)
            stencilIds.Reset()
            return 0

        polys.GetCellPoints(cellIds.GetId(0), ptIds)
        p2 = ptIds.GetId(0)
        i = 1
        while p1 == p2:
            p2 = ptIds.GetId(i)
            i += 1

        polys.GetCellEdgeNeighbors(-1, p1, p2, cellIds)
        nextCell = cellIds.GetId(0)
        bp2 = -1
        bp1 = p2
        if cellIds.GetNumberOfIds() == 1:
            startCell = -1
        else:
            startCell = cellIds.GetId(1)

        stencilIds.Reset()
        stencilIds.InsertNextId(p2)

        j = 0
        while j < numCellsInLoop:
            cell = polys.GetCell(nextCell)
            p = -1
            for i in range(3):
                if cell.GetPointId(i) != p1 and cell.GetPointId(i) != p2:
                    p = cell.GetPointId(i)
                    break
            p2 = p
            stencilIds.InsertNextId(p2)
            polys.GetCellEdgeNeighbors(nextCell, p1, p2, cellIds)
            if cellIds.GetNumberOfIds() != 1:
                bp2 = p2
                j += 1
                break
            nextCell = cellIds.GetId(0)
            j += 1

        nextCell = startCell
        p2 = bp1
        j = 0
        while j < numCellsInLoop and startCell != -1:
            cell = polys.GetCell(nextCell)
            p = -1
            for i in range(3):
                if cell.GetPointId(i) != p1 and cell.GetPointId(i) != p2:
                    p = cell.GetPointId(i)
                    break
            p2 = p
            stencilIds.InsertNextId(p2)
            polys.GetCellEdgeNeighbors(nextCell, p1, p2, cellIds)
            if cellIds.GetNumberOfIds() != 1:
                bp1 = p2
                break
            nextCell = cellIds.GetId(0)
            j += 1

        if bp2 != -1:
            stencilIds.SetNumberOfIds(3)
            stencilIds.SetId(0, bp2)
            stencilIds.SetId(1, bp1)
            stencilIds.SetId(2, p1)
            weights[0] = 0.125
            weights[1] = 0.125
            weights[2] = 0.75
        else:
            K = stencilIds.GetNumberOfIds()
            K -= 1
            if K > 3:
                cosSQ = 0.375 + 0.25 * math.cos(2.0 * vtk.vtkMath.Pi() / float(K))
                cosSQ = cosSQ * cosSQ
                beta = (0.625 - cosSQ) / float(K)
            else:
                beta = 3.0 / 16.0
            for j in range(K):
                weights[j] = beta
            weights[K] = 1.0 - K * beta
            stencilIds.SetId(K, p1)
        return 1

    def GenerateOddStencil(self, p1, p2, polys, stencilIds, weights):
        cellIds = vtk.vtkIdList()
        cell0 = cell1 = p3 = p4 = 0

        polys.GetCellEdgeNeighbors(-1, p1, p2, cellIds)
        cell0 = cellIds.GetId(0)
        cell1 = cellIds.GetId(1)

        cell = polys.GetCell(cell0)
        for i in range(3):
            if cell.GetPointId(i) != p1 and cell.GetPointId(i) != p2:
                p3 = cell.GetPointId(i)
                break
        cell = polys.GetCell(cell1)
        for i in range(3):
            if cell.GetPointId(i) != p1 and cell.GetPointId(i) != p2:
                p4 = cell.GetPointId(i)
                break

        stencilIds.SetNumberOfIds(4)
        stencilIds.SetId(0, p1)
        stencilIds.SetId(1, p2)
        stencilIds.SetId(2, p3)
        stencilIds.SetId(3, p4)

        for i in range(stencilIds.GetNumberOfIds()):
            weights[i] = self.LoopWeights[i]

    def RequestUpdateExtent(self, request, inputVector, outputVector):
        inInfo = inputVector.GetInformationObject(0)
        outInfo = outputVector.GetInformationObject(0)

        if not self.Superclass.RequestUpdateExtent(request, inputVector, outputVector):
            return 0

        numPieces = outInfo.Get(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_NUMBER_OF_PIECES())
        ghostLevel = outInfo.Get(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_NUMBER_OF_GHOST_LEVELS())

        if numPieces > 1 and self.NumberOfSubdivisions > 0:
            inInfo.Set(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_NUMBER_OF_GHOST_LEVELS(), ghostLevel + 1)

        return 1


icosahedron = utils.CreateIcosahedron(1.1,1)
num_vertices = icosahedron.GetNumberOfPoints()
faces = icosahedron.GetNumberOfCells()  # Get the number of faces
print("Number of vertices: ", num_vertices)

# Apply the Loop subdivision filter
subdivisionFilter = vtkLoopSubdivisionFilter()
subdivisionFilter.SetInputData(icosahedron)
subdivisionFilter.Update()
# Print the number of faces in the output mesh
print("Number of points:", subdivisionFilter.GetOutput().GetNumberOfPoints())
print("Number of faces:", subdivisionFilter.GetOutput().GetNumberOfPoints())

# Visualize the original and subdivided meshes
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(subdivisionFilter.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderWindow.Render()
renderWindowInteractor.Start()