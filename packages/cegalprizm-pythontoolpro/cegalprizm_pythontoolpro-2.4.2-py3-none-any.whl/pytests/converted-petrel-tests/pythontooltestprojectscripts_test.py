# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import io
import os
import sys
import pytest
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class Testpythontooltestproject:

    
    def test_HorizonParents(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        horizon_interpretation = petrellink._get_horizon_interpretation('Input/Seismic/Interpretation folder 1/BCU')
        horizon_interpretation.readonly = False
        horizon_interpretation_3d = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
        horizon_interpretation_3d.readonly = False
        try:
            horizon_attribute = horizon_interpretation_3d.horizon_property_3ds[1]
            
            if horizon_attribute.horizon_interpretation_3d.petrel_name != horizon_interpretation_3d.petrel_name:
                print(f"{horizon_attribute.horizon_interpretation_3d.petrel_name} != {horizon_interpretation_3d.petrel_name}")
                print(False)
            if horizon_interpretation_3d.horizon_interpretation.petrel_name != horizon_interpretation.petrel_name:
                print(f"{horizon_interpretation_3d.horizon_interpretation.petrel_name} != {horizon_interpretation.petrel_name}")
                print(False)
            if horizon_attribute.horizon_interpretation_3d.petrel_name == horizon_interpretation_3d.petrel_name and horizon_interpretation_3d.horizon_interpretation.petrel_name == horizon_interpretation.petrel_name:
                print(True)
            else:
                print(False)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizon_parents_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GrpcConnection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            a = petrellink.ping()
            b = petrellink.ping()
            print(b-a)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grpc_connection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteAsDataframe(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        facies = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        facies.readonly = False
        try:
            facies_values = facies.as_dataframe()
            print(facies_values.iloc[7500:7505,3:8])
            
            import copy
            old = copy.deepcopy(facies.samples)
            
            facies.set_values([], [])
            
            print(facies.as_dataframe().iloc[7500:7505,3:8])
            
            facies.samples = old
            facies_values = facies.as_dataframe()
            print(facies_values.iloc[7500:7505,3:8])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_as_dataframe_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteSamplesCount(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        var.readonly = False
        try:
            print(len(var.samples))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_samples_count_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteSetEmpty(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        var.readonly = False
        try:
            import copy
            old = copy.deepcopy(var.samples)
            try:
                var.set_values([], [])
                print(len(var.samples))
            finally:
                var.samples = old
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_set_empty_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteWell(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        facies = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        facies.readonly = False
        try:
            print(facies.well)
            print(facies.global_well_log)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_well_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteSamplesValues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        var.readonly = False
        try:
            print(var.samples[7400:7402])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_samples_values_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogdiscreteSamplesValues2017(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Facies', discrete = True)
        var.readonly = False
        try:
            print(var.samples[7400:7402])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllogdiscrete_samples_values_2017_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteChunkError(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        prop = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Layers', discrete = True)
        prop.readonly = False
        try:
            try:
                prop.chunk((70,200),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((150,160),(40,45),(150,900))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((70,60),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((70,202),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_chunk_error_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        prop = petrellink._get_grid_property('Models/Structural grids/Model_Crazy/Properties/Facies', discrete = True)
        prop.readonly = False
        try:
            print(prop.readonly)
            
            chunk = prop.chunk((10,15),(50,55),(500,505))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = 2
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().iloc[100:103])
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().iloc[100:103])
            
            #Try set non-integer values -should raise ValueError
            df.loc[:,'Value_new'] = 2.05
            try:
                chunk.set(df, 'Value_new')
            except ValueError as err:
                print(err)
            print(chunk.as_dataframe().iloc[100:103])
            
            df.loc[:,'Value_new'] = 2
            
            
            #rename columns in df
            column_names = ["X", "J", "K", "Value1", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            #set with df - incorrect input - no default 'Value' column in df
            print(df.columns.to_list())
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
                
            #set with df - incorrect input - no specified column 'Col'
            print(df.columns.to_list())
            try:
                chunk.set(df, 'Col')
            except Exception as err:
                print(err)
                
            #rename columns
            column_names = ["X", "Y", "Z", "Value", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            #set with df - correct input but no columns I, J, K in df
            print(df.columns.to_list())
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            #rename columns
            column_names = ["i", "j", "k", "Value", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            df_backup = df
            df.drop(labels=df.index[0], inplace = True)
            
            #set with df - incorrect input - no. of rows
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            df = df_backup
            df.drop(labels=df.index[-1], inplace = True)
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
                
            df = df_backup
            df.drop(labels=df.index[-100], inplace = True)
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            chunk.set(df_to_reset_values)
            print(chunk.as_dataframe().iloc[100:103])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteLayer(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            
            original_vals = var.layer(5).as_array()
            
            #Sets the layer value to '1
            for (i,j,k,val) in var.layer(5).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                if i == 0:
                    break
            
            var.layer(5).set(1)
            
            
            for (i,j,k,val) in var.layer(5).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                if i == 0:
                    break
            
            # reset the value
            var.layer(5).set(original_vals)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_layer_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridCoordsextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #prints the world co-ordinates of the Grid
            print(var.coords_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_coordsextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridExtent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #Prints the number of cells in i, j, k directions
            
            print((var.extent.i))
            print((var.extent.j))
            print((var.extent.k))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_extent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridGridvertices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #prints the values are the 8 vertices of the cell, by importing Grid "Vertices"
            from cegalprizm.pythontool import vertices
            
            verts = var.vertices(1,1,1)
            print((len(verts)))
            
            print ('\n'.join([str(v) for v in verts]))
            
            
            #---OR---
            #for index in range(length):
                #print verts[index]
                
            #print verts[vertices.BaseSouthWest]
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_gridvertices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridIndicesValueError(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #ValueErrorException is thrown when position is not in the grid
            print(var.indices(38130, 6223703, -8853))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_indices_value_error_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridIsundefFalse(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #Returns False is the cell is undefined at the given indices
            print(var.is_undef_cell(1,1,1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_isundef_false_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridPetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridPosition(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            # The position of the cell center in world co-ordinates is printed
            print(var.position(1, 1, 1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_position_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridPositionValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #ValueError is thrown if (i,j,k) is outside the grid
            print(var.position(-1, 1, 1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_position_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_GridVertices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #Prints the position at the 8 verticies of a cell at given (i,j,k)
            print([str(v) for v in var.vertices(1,1,1)])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_vertices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridVerticesunchecked(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #Returns the position of the vertices of the cell
            print([str(v) for v in var.vertices_unchecked(1,1,1)])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_verticesunchecked_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridVerticesuncheckedValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #ValueError if the cell is outside the grid
            print(var.vertices_unchecked(1,1,-1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_verticesunchecked_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridVerticesValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #ValueError is output when the cell vertices does not exist
            print(var.vertices(1,1,-1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_vertices_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridIndices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid('Models/Structural grids/Model_Good')
        var.readonly = True
        try:
            #Returns the Indices of the cell at the given (x,y,z) co-ordinates
            print(var.indices(483310, 6225090, -8852))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\grid_indices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_GridpropertyChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        prop = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        prop.readonly = False
        try:
            print(prop.readonly)
            
            chunk = prop.chunk((10,15),(50,55),(500,505))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] * 2
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().iloc[100:103])
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().iloc[100:103])
            
            #rename columns in df
            column_names = ["X", "J", "K", "Value1", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            #set with df - incorrect input - no default 'Value' column in df
            print(df.columns.to_list())
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
                
            #set with df - incorrect input - no specified column 'Col'
            print(df.columns.to_list())
            try:
                chunk.set(df, 'Col')
            except Exception as err:
                print(err)
                
            #rename columns
            column_names = ["X", "Y", "Z", "Value", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            #set with df - correct input but no columns I, J, K in df
            print(df.columns.to_list())
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            #rename columns
            column_names = ["i", "j", "k", "Value", "Value_new"]
            zip_iterator = zip(df.columns.to_list(), column_names)
            a_dictionary = dict(zip_iterator)
            
            df.rename(columns=a_dictionary, inplace = True)
            
            df_backup = df
            df.drop(labels=df.index[0], inplace = True)
            
            #set with df - incorrect input - no. of rows
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            df = df_backup
            df.drop(labels=df.index[-1], inplace = True)
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
                
            df = df_backup
            df.drop(labels=df.index[-100], inplace = True)
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
            chunk.set(df_to_reset_values)
            print(chunk.as_dataframe().iloc[100:103])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyChunkSetDfReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        prop = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        prop.readonly = True
        try:
            print(prop.readonly)
            chunk = prop.chunk((10,15),(50,55),(500,505))
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] * 2
            
            #set with df - correct input on readonly chunk
            print(df.columns.to_list())
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_chunk_set_df_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyChunkError(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        prop = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        prop.readonly = False
        try:
            try:
                prop.chunk((70,200),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((150,160),(40,45),(150,900))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((70,60),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
                
            try:
                prop.chunk((70,202),(40,45),(150,155))
            except Exception as err:
                print(err)
                print('---')
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_chunk_error_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyColumns(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            original_column_00 = var.column(0, 0).as_array()
            original_column_01 = var.column(0, 1).as_array()
            original_column_10 = var.column(1, 0).as_array()
            original_column_11 = var.column(1, 1).as_array()
            
            #sets the value to 0 for islice = 0 & 1, can see the change in 3D window
            for col in var.columns(irange=list(range(0, 2)), jrange=None):
                col.set(0)
                    
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
            
            for (i,j,k, val) in var.column(1,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                
            for (i,j,k, val) in var.column(2,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
            
            # Reset values
            var.column(0, 0).set(original_column_00)
            var.column(0, 1).set(original_column_01)
            var.column(1, 0).set(original_column_10)
            var.column(1, 1).set(original_column_11)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_columns_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyColumnsvalueerrorIrange(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if i-index of slice is inavlid
            for col in var.columns(irange=list(range(-1, 1)), jrange=list(range(0,1))):
                col.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_columnsvalueerror_irange_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyColumnsvalueerrorJrange(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if jrange index is not valid
            for col in var.columns(irange=list(range(0, 1)), jrange=list(range(-1,1))):
                col.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_columnsvalueerror_jrange_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyColumnvalueerrorI(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if i-index is not valid
            for (i,j,k, val) in var.column(-1,0).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_columnvalueerror_i_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyColumnvalueerrorJ(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if j-index is not valid
            for (i,j,k, val) in var.column(0,-1).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_columnvalueerror_j_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_GridpropertyIsundefvalueFalse(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #Returns False if the number is not "NAN"
            #[0, 0, 0] == 2147483647]
            
            with var.column(0,0).values() as vals:
                vals[0] = 55
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k==0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                    print(var.is_undef_value(val))
                    break;
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_isundefvalue_false_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyIsundefvalueTrue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #returns True is the value is 'nan'
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 10:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                    print(var.is_undef_value(val))
                    break;
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_isundefvalue_true_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyLayer(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/VShale')
        var.readonly = False
        try:
            #changes the layer value, can see the changes in 3D window
            for (i,j,k, val) in var.layer(5).enumerate():
                if i == 0:
                    oldval = val
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                    break;
                
            var.layer(5).set(0.11)
                
            for (i,j,k, val) in var.layer(5).enumerate():
                if i == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                    break;
            
            # reset so next test doesn't break
            var.layer(5).set(oldval)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_layer_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyLayers(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #sets the K-slice cells to zero, can see the top layer change in 3D window
            
            originals = []
            for layer in var.layers(list(range(0,1))):
                originals.append(layer.as_array())
                layer.set(0)
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
            
            # Reset values
            ii = 0
            for layer in var.layers(list(range(0,1))):
                layer.set(originals[i])
                i += 1
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_layers_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyLayersvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if k-index is not valid
            for layer in var.layers(list(range(-1,1))):
                layer.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_layersvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyLayervalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #ValueError is thrown if k-index is invalid
            var.layer(-5).set(0.11)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_layervalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyObjectextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #prints the extent of the slice
            print(var.column(0,0).object_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_objectextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyParentcollection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            print(var.parent_collection)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_parentcollection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyParentgrid(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            print(var.grid)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_parentgrid_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyPetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            #prints the petrel name of the parent
            print(var.grid.petrel_name)
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = True
        try:
            #cannot update a Grid property when 'Read only' is checked
            with var.column(0,0).values() as vals:
                vals[0] = 1.23 
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertySetundefvalue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/VShale')
        var.readonly = False
        try:
            
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    oldval = val
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val)) #Expected is [0, 0, 0] == 0] why??
                    print(var.is_undef_value(val))
                    break;
             
             #Reset the value to 'undef value'       
            with var.column(0,0).values() as vals:
                vals[0] = var.undef_value
            
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                    print(var.is_undef_value(val))
                    break;
            
            #reset the value back so following test can pass
            with var.column(0,0).values() as vals:
                vals[0] = oldval
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_setundefvalue_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertySliceclone(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            #trutned object as same values as the original slice
            
            for (i, j, k, val) in var.column(5,5).enumerate():
                if  k ==0:
                    print("[{0} {1} {2}] => {3:.6f}".format(i, j, k, val))
                    break;
                    
            for (i, j, k, val) in var.column(6,5).enumerate():
                if  k ==0:
                    oldval = val
                    print("[{0} {1} {2}] => {3:.6f}".format(i, j, k, val))
                    break;
            
            average_layer = var.column(5,5).clone()
            var.column(6,5).set(average_layer)
            
            for (i, j, k, val) in var.column(6,5).enumerate():
                if  k ==0:
                    print("[{0} {1} {2}] => {3:.6f}".format(i, j, k, val))
                    break;
            
            
            var.column(6,5).set(oldval)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_sliceclone_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertySlicedisconnectedTrue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            #Prints True if the Slice is disconnected
            #[0 1 1] => 0.121630; [0 1 2] => 0.151024...[0 1 3] => 0.136327 because (0.121630+0.151024)/2=0.136327
            
            print(var.layer(3).disconnected)
            for (i, j, k, val) in var.layer(1).enumerate():
                if j == 1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
            
            for (i, j, k, val) in var.layer(2).enumerate():
                if j == 1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
            
            sum_layer = var.layer(1) + var.layer(2)
            average_layer = sum_layer / 2.0
            var.layer(3).set(average_layer)
            
            for (i, j, k, val) in var.layer(3).enumerate():
                if  j ==1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
            
            print(average_layer.disconnected)
            print(var.layer(3).disconnected)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_slicedisconnected_true_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyUnitsymbol(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #reutns the Units for the Model property
            print(var.unit_symbol)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_unitsymbol_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyUpdaterawvalues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Vp')
        var.readonly = False
        try:
            #update the cell value at a given i,j,k
            original = var.column(0,0).as_array()
            
            with var.column(0,0).values() as vals:
                vals[0] = 1.23  
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                if k == 0:
                    break
            
            # Reset values
            var.column(0,0).set(original)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_updaterawvalues_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyUpscaledcellsComplete(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/VShale')
        var.readonly = False
        try:
            try:
                is_oop
            except NameError:
                is_oop = False
            
            if is_oop:
                from cegalprizm.pythontool.primitives import Indices
            
            old_upscaled_cells = var.upscaled_cells
            
            print(len(var.upscaled_cells)) # 2942 for Vs [U]
            var.upscaled_cells = [Indices(1,1,1), Indices(2,2,2)]
            print(len(var.upscaled_cells)) # 2
            print(var.upscaled_cells[1].k) # 2
            var.upscaled_cells = None
            print(len(var.upscaled_cells)) # 0
            
            #restore for next test
            var.upscaled_cells = old_upscaled_cells
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_upscaledcells_complete_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteArithmeticforbidden(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #Arithmetic on discrete slices is forbidden
            try:
                var.layer(1).set(var.layer(1)+2)
                print(False)
            except ValueError as v:
                print("Arithmetic operations are not allowed for chunks of discrete values" in str(v))
                
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_arithmeticforbidden_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteColumns(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            original_vals = dict()
            
            for i in range(0, 2):
                for j in range(0, 1):
                    original_vals[i, j] = var.column(i, j).as_array()
            
            #Values are set in the given irange & jrange
            for col in var.columns(irange=list(range(0, 2)), jrange=list(range(0,1))):
                col.set(0)
                
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
            
            for (i,j,k, val) in var.column(1,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                
            for (i,j,k, val) in var.column(2,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
            
            for i in range(0, 2):
                for j in range(0, 1):
                    var.column(i, j).set(original_vals[i, j])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_columns_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteColumnsvalueerrorIrange(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when i-index is invalid
            for col in var.columns(irange=list(range(-1, 1)), jrange=None):
                col.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_columnsvalueerror_irange_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteColumnsvalueerrorJrange(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when j-index is invalid
            for col in var.columns(irange=list(range(0, 1)), jrange=list(range(-1,1))):
                col.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_columnsvalueerror_jrange_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteColumnvalueerrorI(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown if i-index is invalid
            for (i,j,k, val) in var.column(-1,0).enumerate():
                if k == 0 or k==1:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_columnvalueerror_i_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteColumnvalueerrorJ(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when j-index is invalid
            for (i,j,k, val) in var.column(0,-1).enumerate():
                if k == 0 or k==1:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_columnvalueerror_j_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteDiscretecode(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #Discrete code is changed from 'Fine sand' to 'Sand sand'. This does not affect the Petrel object
            var.discrete_codes[1] = "Sand sand"
            print(var.discrete_codes)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_discretecode_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_GridpropertydiscreteIsundef(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #Returns False if the value is not a 'nan' for Discrete Model property
            for (i,j,k, val) in var.column(0,0).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                if k == 0:
                    print(var.is_undef_value(val))
                    break;
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_isundef_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteIsundefvalueFalse(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            original_vals = var.column(0, 0).as_array()
            
            #Prints False because the value is set to a non-undef value for Discrete property
            with var.column(0,0).values() as vals:
                vals[0] = 55
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k==0:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                    print(var.is_undef_value(val))
                    break;
            
            var.column(0, 0).set(original_vals)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_isundefvalue_false_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteIsundefvalueTrue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #Returns False if the value is not a 'nan' or 'MAX_INT'=2147483647 for Discrete Model property
            for (i,j,k, val) in var.column(1,1).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val)) #value returned 241400000 hence failing
                if k == 0:
                    print(var.is_undef_value(val))
                    break;
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_isundefvalue_true_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteLayers(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            original_vals = dict()
            
            for k in range(2, 3):
                original_vals[k] = var.layer(0).as_array()
            
            #Cells in layers 2 and 3 are all set to 66, can see the change in 3D Window
            for layer in var.layers(krange=(2,3)):
                layer.set(66)
                
            for (i,j,k, val) in var.column(78,53).enumerate():
                if k==1 or k==2 or k==3 or k==4:
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                    
            for k in range(2, 3):
                var.layer(0).set(original_vals[k])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_layers_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteLayersvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown if k-index is invalid
            for layer in var.layers(list(range(-1,1))):
                layer.set(0)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_layersvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteLayervalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when k-index is invalid
            var.layer(-5).set(1)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_layervalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteParentcollection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            print(var.parent_collection)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_parentcollection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteParentgrid(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            print(var.grid)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_parentgrid_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscretePetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #prints Petrel name
            print(var.petrel_name)
            print(var.grid.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = True
        try:
            #Cannot overwrite the values when 'Read only' is checked on
            with var.column(0,0).values() as vals :
                vals[0] = 111
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = True
        try:
            print(var.retrieve_stats()['Max'])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteSetundefvalue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #First set the value to a 'not undef' value
            with var.column(0,0).values() as vals:
                original_val = vals[0]
                vals[0] = int(1) 
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if (not var.is_undef_value(val)):
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val) + " value is not undef")
                    break
            
            #set the value to an 'undef' value 
            with var.column(0,0).values() as vals:
                vals[0] = var.undef_value
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if (var.is_undef_value(val)):
                    print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val) + " value is undef")
                    break
            
            with var.column(0,0).values() as vals:
                vals[0] = original_val
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_setundefvalue_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteUnitsymbol(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #print None for Facies - a discrete Grid Property template
            print(var.unit_symbol)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_unitsymbol_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertydiscreteUpdaterawvalues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            #update the cell value at a given i,j,k for a Discrete Grid proeprty
            with var.column(0,0).values() as vals:
                original_val = vals[0]
                vals[0] = 1.23  
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                print("[{0}, {1}, {2}] == {3}]".format(i,j,k,val))
                if k == 0:
                    break;
            
            with var.column(0,0).values() as vals:
                vals[0] = original_val
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridpropertydiscrete_updaterawvalues_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizoninterpretation3d(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
        var.readonly = False
        try:
            try:
                is_oop
            except NameError:
                is_oop = False
            
            ok = True
            if var.sample_count != 120908:
                ok = False
                print("var.sample_count != 120908\n")
                print(var.sample_count)
            if str(var) != "HorizonInterpretation3D(petrel_name=\"Ardmore\")":
                ok = False
                print("str(var) != \"HorizonInterpretation3D(petrel_name=\"Ardmore\")\"")
            if var.unit_symbol != "ms":
                ok = False
                print("var.unit_symbol != \"ms\"")
            if int(var.position(20, 30).x) != 486458:
                ok = False
                print("int(var.position(20, 30).x) != 486458\n")
                print(int(var.position(20, 30).x))
            if var.indices(486288.6570124189, 6223608.341706959).i != 30:
                ok = False
                print("var.indices(486288.6570124189, 6223608.341706959).i != 30")
                print(var.indices(486288.6570124189, 6223608.341706959).i)
            
            chunk_0 = var.chunk((4,5), (4, 5))
            data = chunk_0.as_array().flat
            data_vec = [v for v in data]
            if 4 != len(data_vec):
                ok = False
                print("4 != len(data_vec)")
            if [int(v) for v in data_vec] != [-2654, -2654, -2654, -2655]:
                ok = False
                print("[int(v) for v in data_vec] != [-2654, -2654, -2654, -2655]\n")
                print([int(v) for v in data_vec])
            chunk_1 = var.chunk((4,4), (4,4))
            chunk_1.set(42)
            chunk_2 = var.chunk((4,5), (4, 5))
            new_data_vec = [int(v) for v in chunk_2.as_array().flat]
            if [int(v) for v in new_data_vec] != [42, -2654, -2654, -2655]:
                ok = False
                print("[int(v) for v in new_data_vec] != [42, -2654, -2654, -2655]")
                print([int(v) for v in new_data_vec])
            chunk_1.set(data_vec[0])
            
            var_prp = var.horizon_property_3ds[1]
            if is_oop:
                var_prp.readonly = False
            if str(var_prp) != "HorizonProperty3D(petrel_name=\"Autotracker: Confidence\")":
                ok = False
                print("str(var_prp) != \"HorizonProperty3D(petrel_name=\"Autotracker: Confidence\")\"\n")
                print(str(var_prp))
            if int(var_prp.position(20, 30).x) != 486458:
                ok = False
                print("int(var_prp.position(20, 30).x) != 486458\n")
                print(int(var_prp.position(20, 30).x))
            if var_prp.indices(486288.6570124189, 6223608.341706959).i != 30:
                ok = False
                print("var_prp.indices(486288.6570124189, 6223608.341706959).i != 30\n")
                print(var_prp.indices(486288.6570124189, 6223608.341706959).i)
            
            chunk_prp_0 = var_prp.chunk((4,5), (4, 5))
            data_prp = chunk_prp_0.as_array().flat
            data_prp_vec = [v for v in data_prp]
            if 4 != len(data_prp_vec):
                ok = False
                print("4 != len(data_prp_vec)")
            if [int(v) for v in data_prp_vec] != [0, 0, 0, 0]:
                ok = False
                print("[int(v) for v in data_prp_vec] != [0, 0, 0, 0]\n")
                print([int(v) for v in data_prp_vec])
            chunk_prp_1 = var_prp.chunk((4,4), (4,4))
            chunk_prp_1.set(42)
            chunk_prp_2 = var_prp.chunk((4,5), (4, 5))
            new_data_vec = [int(v) for v in chunk_prp_2.as_array().flat]
            if [int(v) for v in new_data_vec] != [42, 0, 0, 0]:
                ok = False
                print("[int(v) for v in new_data_vec] != [42, 0, 0, 0]\n")
                print([int(v) for v in new_data_vec])
            chunk_prp_1.set(data_prp_vec[0])
            print(ok)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation3D_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizoninterpretation3dCrs(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
        var.readonly = False
        try:
            print("START")
            ok = True
            if var.crs_wkt is None:
                ok = False
            if int(var.affine_transform[0]) != 6:
                ok = False
            
            var_prp = var.horizon_property_3ds[1]
            if var_prp.crs_wkt is None:
                ok = False
            if int(var_prp.affine_transform[0]) != 6:
                ok = False
            print(ok)
            print("END")
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation3D_crs_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizoninterpretation(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        hi = petrellink._get_horizon_interpretation('Input/Seismic/Interpretation folder 1/BCU')
        hi.readonly = False
        try:
            print(hi)
            print([v for v in hi.horizon_interpretation_3ds])
            print([v.horizon_interpretation for v in hi.horizon_interpretation_3ds])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizoninterpretation1Clone(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            hi = petrellink._get_horizon_interpretation('Input/Seismic/Interpretation folder 1/BCU')
            try:
                hi_clone = hi.clone('BCU_copy', copy_values = True)
            except Exception as e:
                hi_clone = petrellink._get_horizon_interpretation('Input/Seismic/Interpretation folder 1/BCU_copy')
            
            print(hi_clone)
            
            print([v for v in hi.horizon_interpretation_3ds])
            print([v.horizon_interpretation for v in hi.horizon_interpretation_3ds])
            print([v for v in hi_clone.horizon_interpretation_3ds])
            print([v.horizon_interpretation for v in hi_clone.horizon_interpretation_3ds])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation1_clone_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogAsDataframe(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        vp = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vp')
        vp.readonly = False
        try:
            vp_values = vp.as_dataframe()
            print(vp_values.iloc[500:505,3:8])
            
            import copy
            old = copy.deepcopy(vp.samples)
            vp.set_values([], [])
            
            print(vp.as_dataframe().iloc[500:505,3:8])
            
            vp.samples = old
            vp_values = vp.as_dataframe()
            print(vp_values.iloc[500:505,3:8])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_as_dataframe_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesAt(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            print(var.samples.at(5812).value)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_at_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesSetValues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            import copy
            old = copy.deepcopy(var.samples)
            try:
                var.set_values([1, 2, 3], [1.1, 2.2, 3.3])
                print(len(var.samples))
                print("{:.4f}".format(var.samples.at(2).value))
            finally:
                var.samples = old
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_set_values_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesSetValuesEmpty(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            import copy
            old = copy.deepcopy(var.samples)
            try:
                var.set_values([], [])
                print(len(var.samples))
            finally:
                var.samples = old
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_set_values_empty_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesSetWritable(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            old = var.samples.at(5812).value
            try:
                var.samples.at(5812).value = 123
                for s in var.samples[200:202]:
                    print(s.value)
            finally:
                var.samples.at(5812).value = old
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_set_writable_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesCount(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            print(len(var.samples))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_count_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesTransferInBulk(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        vs = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        vs.readonly = False
        vp = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vp')
        vp.readonly = False
        try:
            # record values as we're futzing with them
            a_vs = vs.samples.at(5812).value
            a_vp = vp.samples.at(5812).value
            import copy
            old = copy.deepcopy(vp.samples)
            try:
                vp.samples = vs.samples
                print(vp.samples.at(5812).value == a_vs)
            finally:
                vp.samples = old
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_transfer_in_bulk_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesValues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            print('[' + ', '.join([str(sample) for sample in var.samples[200:202]]) + ']')
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_values_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSamplesValues2017(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
        var.readonly = False
        try:
            print(var.samples[200:202])
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_samples_values_2017_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogNavigation(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            from datetime import datetime
            
            start = datetime.now()
            
            for well in petrellink.wells:
                for log in well.logs:
                    print(log)
            
            print(datetime.now() - start)
            
            print("Ok")
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_navigation_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WelllogSetvalues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        vp = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vp')
        vp.readonly = False
        try:
            vp_values = vp.as_dataframe()
            
            print(vp_values.iloc[500:505,3:8])
            
            md = vp_values["MD"].values
            vp_log_values = vp_values["Value"].values
            vp_log_values_new = vp_log_values * 1.55
            
            vp.set_values(md,vp_log_values_new)
            print(vp.as_dataframe().iloc[500:505,3:8])
            
            vp.set_values(md,vp_log_values)
            print(vp.as_dataframe().iloc[500:505,3:8])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\welllog_setvalues_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_PetrelbridgeGridkeyvalueOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            myprop = petrellink.grids
            for (path, value) in sorted(list(myprop.items()), key = lambda p: str(p[1])):
                s = path
                if not value.path.endswith('_copy'):
                    print("[{0}=={1}]".format(s, value))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelbridge_gridkeyvalue_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelbridgeGridPathOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            # Paths to all grids
            grids = petrellink.grids
            
            for (guid, grid) in sorted(list(grids.items()), key = lambda p: p[1].path):
                print(grid.path)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelbridge_grid_path_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))

    def test_PetrelbridgeGridOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            # prints all the grids
            for (name, prop) in sorted(list(petrellink.grids.items()), key = lambda p: p[1].petrel_name):
                print("* => {0}".format(prop.petrel_name))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelbridge_grid_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelconnectionMakeConnection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            from cegalprizm.pythontool import  make_connection
            import numpy as np
            import pandas as pd
            
            with make_connection() as p:
                    print(p.a_project_is_active())
                    print(p.get_current_project_name())
                    
                    #checking writing from and to Petrel
                    GR = p.well_logs['Input/Wells/Well_Good/Well logs/GR']
                    GR_clone = GR.clone('Copy of GR', True)
                    
                    df = GR_clone.as_dataframe()
                    print(df.head().take([0,1,2,3,4,5], axis=1))
                    
                    MD_to_reset = np.array(df["MD"])
            
                    df["MD"] = df["MD"] + 10
                    GR_clone.set_values(np.array(df["MD"]),np.array(df["Value"]))
                    df_clone_after_set_values = GR_clone.as_dataframe()
                    print(df_clone_after_set_values.head().take([0,1,2,3,4,5], axis=1))
            
                    GR_clone.set_values(MD_to_reset,np.array(df["Value"]))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelconnection_make_connection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Crs(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            print("START")
            hi3d = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
            well = petrellink._get_well('Input/Wells/Well_Good')
            welllog = petrellink._get_well_log('Input/Wells/Well_Good/Well logs/Vs')
            pointset = petrellink._get_pointset('Input/Geometry/Seismic_pointset')
            polylineset = petrellink._get_polylineset('Input/Geometry/Polygon')
            cube = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
            line = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
            surface = petrellink._get_surface('Input/TWT Surface/BCU')
            surfaceattribute = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
            hp3d = hi3d.horizon_property_3ds[1]
            domainobjects = [petrellink, hi3d, well, pointset, polylineset, cube, line, surface, surfaceattribute, hp3d ]
            domainobjects_with_transform = [ hi3d, cube, surface, surfaceattribute, hp3d ]
            ok = True
            
            for o in domainobjects:
                try:
                    if not type(o.crs_wkt) is str:
                        ok = False
                except Exception as e:
                    print(f"Problem with {o}, threw exception {e}")
                    ok = False
            
            for o in domainobjects_with_transform:
                try:
                    if len(o.affine_transform) != 6:
                        ok = False
                except Exception as e:
                    print(f"Problem with {o}, threw exception {e}")
                    ok = False
                
            print(ok)
            print("END")
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\crs_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelconnectionAProjectIsActiveOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            print(petrellink.a_project_is_active())
            print(petrellink.get_current_project_name())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelconnection_a_project_is_active_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelconnectionOpenDeprecation(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            import warnings
            warnings.filterwarnings("error", category=DeprecationWarning)
            try:
                petrellink.open()
                print("failed")
            except Exception as e:
                print("ok")
            warnings.resetwarnings()
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelconnection_open_deprecation_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelconnectionGetprojectstorageunits(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            for k, v in sorted(list(petrellink.get_petrel_project_units().items())):
                print(k, v)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelconnection_getprojectstorageunits_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PetrelobjectDroid(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            print(petrellink.discrete_global_well_logs['Input/Wells/Global well logs/Facies'].droid)
            print(petrellink.discrete_grid_properties['Models/Structural grids/Model_NoData/Properties/Facies'].droid)
            print(petrellink.discrete_grid_properties['Models/Structural grids/Model_NoData/Properties/Facies'].droid)
            print(petrellink.discrete_surface_attributes['Input/TWT Surface/BCU/Facies'].droid)
            print(petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies'].droid)
            print(petrellink.global_well_logs['Input/Wells/Global well logs/LambdaRho'].droid)
            print(petrellink.grid_properties['Models/Structural grids/Model_Good/Properties/AI'].droid)
            print(petrellink.grids['Models/Structural grids/Model_NoProperties'].droid)
            print(petrellink.horizon_interpretation_3ds['Input/Seismic/Interpretation folder 1/BCU/Ardmore'].droid)
            print(petrellink.horizon_properties['Input/Seismic/Interpretation folder 1/BCU/Ardmore/TWT'].droid)
            print(petrellink.pointsets['Input/Geometry/Points empty'].droid)
            print(petrellink.polylinesets['Input/Geometry/Polygon'].droid)
            print(petrellink.grid_properties['Models/Structural grids/Model_NoData/Properties/Rho'].droid)
            print(petrellink.property_collections['Models/Structural grids/Model_NoProperties/Properties'].droid)
            print(petrellink.seismic_2ds['Input/Seismic/Survey 1/Seismic2D'].droid)
            print(petrellink.seismic_cubes['Input/Seismic/Survey 2/Tiny3D'].droid)
            print(petrellink.seismic_lines['Input/Seismic/Survey 1/Seismic2D'].droid)
            print(petrellink.surface_attributes['Input/TWT Surface/BCU/TWT'].droid)
            print(petrellink.surface_discrete_attributes['Input/TWT Surface/BCU/Facies'].droid)
            print(petrellink.surfaces['Input/TWT Surface/BCU'].droid)
            print(petrellink.well_logs['Input/Wells/Well_Good/Well logs/Vp_K'].droid)
            print(petrellink.wells['Input/Wells/Well_Good'].droid)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\petrelobject_droid_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PolylinesetComplete(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_polylineset('Input/Geometry/Polygon')
        var.readonly = False
        try:
            try:
                is_oop
            except NameError:
                is_oop = False
            
            if is_oop:
                from cegalprizm.pythontool import Point
            
            old_positions = var[0].positions()
            print(var.petrel_name) # Polygon
            print(len(var)) # 1
            print(var[0]) # Polyline(parent_polylineset=PolylineSet(petrel_name="Polygon"))
            print(var[0].polylineset) #PolylineSet(petrel_name="Polygon")
            var.add_line([Point(0,0,0), Point(1,1,1), Point(2,2,2)])
            print(var[1].points[2].x) # 2.0
            var.delete_line(var[0])
            print(var[0].points[1].x) # 1.0
            print(len(var[0].points)) # 3
            print(var[0].readonly) # False
            print(var[0].closed) # True
            print(var.is_closed(0)) # True
            var[0].add_point(Point(3,3,3))
            print(len(var[0].points)) # 4
            var[0].delete_point(Point(1,1,1))
            print([p.x for p in var[0].points]) # [0.0, 2.0, 3.0]
            print(var[0].positions()) # [[0.0, 2.0, 3.0], [0.0, 2.0, 3.0], [0.0, 2.0, 3.0]]
            print(var.get_positions(0)) # [[0.0, 2.0, 3.0], [0.0, 2.0, 3.0], [0.0, 2.0, 3.0]]
            print(var.retrieve_stats()['Number of polygons']) # 1
            for line in var.polylines:
                print(line)
            var.set_positions(0,[10.0, 2.0, 3.0], [10.0, 2.0, 3.0], [10.0, 2.0, 3.0])
            print(var.get_positions(0))
            var.set_positions(0, *old_positions)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\polylineset_complete_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PolylinesetGetpoints(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_polylineset('Input/Geometry/Polygon')
        var.readonly = False
        try:
            print(str(type(var.get_positions(0)))[-7:-2])
            print(["{:.2f}".format(v) for item in var.get_positions(0) for v in item])
            pol = var[0]
            print(pol)
            print(str(type(pol.positions()))[-7:-2])
            print(["{:.2f}".format(v) for item in pol.positions() for v in item])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\polylineset_getpoints_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_PolylinesetCompleteReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_polylineset('Input/Geometry/Polygon')
        var.readonly = True
        try:
            try:
                var.add_line([Point(0,0,0), Point(1,1,1), Point(2,2,2)])
            except:
                print("caught")
            try:
                var.delete_line(var[0])
            except:
                print("caught")
            
            print(var[0].readonly) # True
            
            try:
                var[0].add_point(Point(3,3,3))
            except:
                print("caught")
            
            try:
                var[0].delete_point(var[0].points[0])
            except:
                print("caught")
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\polylineset_complete_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Propertycollection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            grid_properties = [gp for gp in var.parent_collection if not gp.petrel_name.endswith('_copy')] 
            print(len(grid_properties))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\propertycollection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dChunkSetOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            newline = var.clone('Copy of 2D line', True)
            df_original_values = newline.column(10).as_dataframe()
            print(df_original_values.head())
            newline.column(10).set(7.77)
            print(newline.column(10).as_dataframe().head())
            newline.column(10).set(df_original_values)
            print(newline.column(10).as_dataframe().head())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_chunk_set_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dColumn(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #ValueError is thrown if j-index is invalid
            for (i,j,k, val) in var.column(0).enumerate():
                print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                if k == 0:
                    break;
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_column_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dColumns(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #can access the column slices
            for cols in var.columns(jrange=(0,1)):
                for (i,j,k, val) in cols.enumerate():
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                    if k==1:
                        break;
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_columns_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dColumnsvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #ValueError is thrown when the i-index is invalid
            for cols in var.columns(jrange=(-1,1)):
                for (i,j,k, val) in cols.enumerate():
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                    if k==1:
                        break;
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_columnsvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dCoordsextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #prints the seismic's World coordinates
            print(var.coords_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_coordsextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dExtent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #prints the extents in j,k direction. i will always be 'None'
            print(var.extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_extent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dHassameparent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        var_1 = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var_1.readonly = False
        try:
            print(var.has_same_parent(var))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_hassameparent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dHassameparentValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        var_1 = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var_1.readonly = False
        try:
            #ValueError is thrown if the other objects is not Seismic 2D line
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_hassameparent_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dIndices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #prints the indices at the given (x,y,z)
            print(var.indices(484799, 6224142, -2400))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_indices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dIndicesvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #ValueError is thrown when (x,y,z) is outside the seismic
            print(var.indices(1,1,1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_indicesvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dPetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #prints Petrel name 
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dPosition(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #prints the (x, y, z) coordinates at a given (j, k) position
            print(var.position(0,0))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_position_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dPositionvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            #ValueError is thrown if position is outside the seismic
            print(var.position(999,0))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_positionvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = True
        try:
            #Cannot write if the Seismic 'Read only' is checked
            with var.column(0).values() as vals:
                vals[0] = 1.23
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic2dRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var.readonly = False
        try:
            print(var.retrieve_stats().get('Number of cells total'))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic2D_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dAll(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            chunk_all = var.all()
            print(var.extent)
            print(chunk_all.object_extent)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_all_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dAnnotation(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints the annotation for seismic indices, default to k=0
            print(var.annotation(0,0,0))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_annotation_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dAnnotationIndices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints the indices of a inline/crossline/sample. Sample defaults to 1
            print(var.annotation_indices(855,2297, 1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_annotation_indices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dAnnotationIndicesValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #throws ValueError when indices of inline/xline/sample are outside the seismic
            print(var.annotation_indices(1,1,1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_annotation_indices_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dAnnotationvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #ValueError exception is thrown when indices is outside the seismic
            print(var.annotation(0,0,-200))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_annotationvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dChunk(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Survey 2/Tiny3D')
        var.readonly = False
        try:
            extent = var.extent
            
            def reset():
                allchunk = var.chunk((), (), ())
                with allchunk.values() as vals:
                    for i in range(0, allchunk.slice_extent.i):
                        for j in range(0, allchunk.slice_extent.j):
                            for k in range(0, allchunk.slice_extent.k):
                                vals[i, j, k] = i + 10 * j + 100 * k
            
            def is_in(idx, idx_tuple):
                if idx_tuple is not None:
                    return idx >= idx_tuple[0] and idx <= idx_tuple[1]
                else:
                    return True
            
            def check_chunk(irange, jrange, krange):
                print("check chunk", irange, jrange, krange)
                reset()
                c = var.chunk(irange, jrange, krange)
                if c.as_array() is None:
                    raise Exception("Chunks values are empty")
                c.set(999.0)
            
                with var.chunk((), (), ()).values() as vals:
                    for i in range(0, extent.i):
                        for j in range(0, extent.j):
                            for k in range(0, extent.k):
                                val = vals[i, j, k]
                                if is_in(i, irange) and is_in(j, jrange) and is_in(k, krange):
                                    if val != 999.0:
                                        raise Exception("failed in chunk")
            
                                elif val != i + j * 10 + k * 100:
                                    raise Exception("failed outside chunk")
            
            possible_is = [None] + list(range(0, extent.i))
            possible_js = [None] + list(range(0, extent.j))
            possible_ks = [None] + list(range(0, extent.k))
            
            import itertools as it
            
            i_s = [None] + [(f, t) for (f, t) in it.combinations(possible_is, 2) if f is not None]
            j_s = [None] + [(f, t) for (f, t) in it.combinations(possible_js, 2) if f is not None]
            k_s = [None] + [(f, t) for (f, t) in it.combinations(possible_ks, 2) if f is not None]
            
            for irange in i_s:
                for jrange in j_s:
                    for krange in k_s:
                        check_chunk(irange, jrange, krange)
            
            print("Ok")
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_chunk_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dSetValue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Survey 2/Tiny3D')
        var.readonly = False
        try:
            extent = var.extent
            chunk_all = var.all()
            original_array = chunk_all.as_array()
            var.set_value(1337.0)
            new_array = var.all().as_array()
            print(abs((new_array - 1337.0).sum()) < 0.05)
            chunk_all.set(original_array)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_set_value_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dChunkError(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            try:
                var.chunk((70,400),(40,45),(150,155)).as_dataframe()
            except Exception as err:
                print(err)
                print('---')
                
            try:
                var.chunk((350,360),(40,45),(150,900)).as_dataframe()
            except Exception as err:
                print(err)
                print('---')
                
            try:
                var.chunk((70,60),(40,45),(150,155)).as_dataframe()
            except Exception as err:
                print(err)
                print('---')
                
            try:
                var.chunk((70,902),(40,45),(150,155)).as_dataframe()
            except Exception as err:
                print(err)
                print('---')
            try:
                var.chunk((-70,-60),(40,45),(150,155)).as_dataframe()
            except Exception as err:
                print(err)
                print('---')
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_chunk_error_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dColumns(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #sets the value to 0 for islice = 0 & 1, can see the change in 3D window. Move the seismic Inline/Xline to islice = 0
            
            original_values = [None]*2
            for i in range(2):
                original_values[i] = [None]*2
                for j in range(2):
                    original_values[i][j] = var.column(i, j).as_array()
            
            for col in var.columns(irange=list(range(0, 2)), jrange=list(range(0,2))):
                col.set(0)
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
            
            for (i,j,k, val) in var.column(1,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
                
            for (i,j,k, val) in var.column(2,0).enumerate():
                if k == 0:
                    print("[{0}, {1}, {2}] == {3:.2f}]".format(i,j,k,val))
            
            
            # Reset to original values
            for i in range(2):
                for j in range(2):
                    var.column(i, j).set(original_values[i][j])
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_columns_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dColumnvalueerrorI(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #ValueError is thrown if i-index is invalid
            with var.column(-1,0).values() as vals:
                vals[0] = 1.23
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_columnvalueerror_i_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dColumnvalueerrorJ(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #ValueError is thrown when j-index is invalid
            with var.column(0,-1).values() as vals:
                vals[0] = 1.23
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_columnvalueerror_j_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dCoordsextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints the world co-ordinates
            print(var.coords_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_coordsextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dExtent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints petrel name
            print(var.extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_extent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dHassameparent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            ardmore_clone = var.clone("Ardmore clone", True)
            print(var.has_same_parent(ardmore_clone))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_hassameparent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dHassameparentValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        var_1 = petrellink._get_seismic_2d('Input/Seismic/Survey 1/Seismic2D')
        var_1.readonly = False
        try:
            #ValueError is thrown if two different objects are compared for same parent
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_hassameparent_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dIndices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints the indices at the given (x,y,z)
            print(var.indices(486496, 6223208, -2400))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_indices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dIndicesvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #ValueError is thrown when (x,y,z) is outside the seismic
            print(var.indices(0,0,0))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_indicesvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dLayers(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            vals = var.layer(0).as_array()
            print("{0:.2f}".format(vals[2,3]))
            
            var.layer(0).set(var.layer(0) * 10)
            vals = var.layer(0).as_array()
            print("{0:.2f}".format(vals[2,3]))
            
            var.layer(0).set(var.layer(0) / 10)
            vals = var.layer(0).as_array()
            print("{0:.2f}".format(vals[2,3]))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_layers_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dObjectextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints the extent of the slice
            print(var.column(0,0).object_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_objectextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dPath(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            seismic = petrellink.seismic_cubes['Input/Seismic/Ardmore/Seismic3D']
            print(seismic.path)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_path_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dPetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #prints petrel name
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dPosition(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #print the world coordinate positon at the given i,j,k
            print(var.position(0,0,0))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_position_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dPositionvalueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #ValueError is thrown when Position is outside the seismic
            print(var.position(555,555,555))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_positionvalueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = True
        try:
            #Cannot overwrite the values when 'Read only' is checked on
            with var.column(0,0).values() as vals :
                vals[0] = 111
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dSliceclone(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            #trutned object as same values as the original slice
            
            for (i, j, k, val) in var.column(10,10).enumerate():
                if  k ==0 or k== 1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
                    
            for (i, j, k, val) in var.column(22,15).enumerate():
                if  k ==0 or k== 1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
            
            average_layer = var.column(10,10).clone()
            oldcolumnvalues = var.column(22,15).as_array()
            var.column(22,15).set(average_layer)
            
            for (i, j, k, val) in var.column(22,15).enumerate():
                if  k ==0 or k== 1:
                    print("[%d %d %d] => %f" % (i, j, k, val))
                    break;
            
            var.column(22, 15).set(oldcolumnvalues)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_sliceclone_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dUpdaterawvalue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            original_value = var.column(0,0).as_array()[0]
                
            with var.column(0,0).values() as vals:
                vals[0] = 1.23  
                
            for (i,j,k, val) in var.column(0,0).enumerate():
                print("[{0}, {1}, {2}] == {3:.2f}".format(i,j,k,val))
                if k == 0:
                    break
            
            # Reset to original value
            with var.column(0,0).values() as vals:
                vals[0] = original_value
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_updaterawvalue_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Seismic3dRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var.readonly = False
        try:
            def mylen(d):
                # Can't use built-in len as CPython doesn't know how to the __len__ of a C# Dictionary, although it can iterate over it (using Python.NET)...
                l = 0
                for k in d:
                    l = l + 1
                return l
            
            print(mylen(var.retrieve_stats()) > 0)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\seismic3D_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceHassameparent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        var_1 = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var_1.readonly = False
        try:
            #Prints True is both properties have same Parent
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_hassameparent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceHassameparentValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        var_1 = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var_1.readonly = False
        try:
            #ValueError is thrown when Surface property is compared with a Seismic cube
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_hassameparent_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceIsundefFalse(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Returns False if it's a valid value, i.e, not NAN
            #[1,1]==-2710.73999023 is a valid number
            print(var.is_undef_value(var.all().as_array()[1,1]))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_isundef_false_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceIsundefTrue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Returns True if the value is NAN
            #First manually set the value to NAN using 'undef-value' and then do the is_undef
            
            layer = var.all().as_array()
            original_value = layer[0,0]
            
            layer[0,0] = var.undef_value
            var.all().set(layer)
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            # Reset
            layer[0,0] = original_value
            var.all().set(layer)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_isundef_true_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceObjectextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #prints the extent of the slice
            print(var.all().object_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_objectextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurface(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Returns the parent Surface of the attribute
            print(var.surface.petrel_name) 
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurface_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceCoordsextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Prints the World coordinates
            print(var.surface.coords_extent)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurface_coordsextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            def mylen(d):
                # Can't use built-in len as CPython doesn't know how to the __len__ of a C# Dictionary, although it can iterate over it (using Python.NET)...
                l = 0
                for k in d:
                    l = l + 1
                return l
            
            print(mylen(var.retrieve_stats()) > 0)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurface_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #prints the maximum i & j indices
            print(var.surface.extent)
            print(var.surface.extent.i)
            print(var.surface.extent.j)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurfaceextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceindices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #prints the indices of the cell at the given (x,y) location
            print(var.surface.indices(484798, 6224426))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurfaceindices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceindicesValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #ValueError is thrown when (x,y) is outside the Surface
            print(var.surface.indices(400, 600))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurfaceindices_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceposition(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Prints the (x,y,z) position of the cell at the given (i,j). z will always be none
            print(var.surface.position(130, 153))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurfaceposition_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfacepositionValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #ValueError is thrown when (i,j) is outside the Surface geometry
            print(var.surface.position(131,154))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurfaceposition_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfacePetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #prints Petrel name of the Surface attribute
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = True
        try:
            #Cannot write to the Surface when 'Read only' is checked
            layer = var.all().as_array()
            layer[0,0] = 0
            var.all().set(layer)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            def mylen(d):
                # Can't use built-in len as CPython doesn't know how to the __len__ of a C# Dictionary, although it can iterate over it (using Python.NET)...
                l = 0
                for k in d:
                    l = l + 1
                return l
            
            print(mylen(var.retrieve_stats()) > 0)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceSetundefvalue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #First set the value to 'undef-value', then change it back to a 'def' value
            layer = var.all().as_array()
            original_value = layer[0,0]
            layer[0,0] = var.undef_value #float('nan')
            var.all().set(layer)
            print(var.all().as_array()[0,0])
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            layer = var.all().as_array()
            layer[0,0] = -2711.13061523
            var.all().set(layer)
            print("{:.2f}".format(var.all().as_array()[0,0]))
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            # Reset to original value
            layer[0, 0] = original_value
            var.all().set(layer)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_setundefvalue_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceUnitsymbol(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #print the Petrel units
            print(var.unit_symbol)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_unitsymbol_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceUpdaterawvalues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            #Uncheck 'Read only' and update the rawvalues using all().set(value)
            #The value is set for the whole surface which has one z slice
            
            # 6/6/18 - this float cast is a massive smell.  The slice.set method 
            # should cope now with numpy floats but doesn't seem to? 
            original_values = var.all().as_array()
            
            a = float(var.all().as_array()[0,0])
            var.all().set(a+100.0)
            
            for (i,j,k,val) in var.all().enumerate():
                print("[{0},{1},{2}]=={3:.2f}]".format(i,j,k,val))
                if j == 1:
                    break
            
            # Reset values
            var.all().set(original_values)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_updaterawvalues_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceParentsurfaceSurfaceattributes(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            print(len(var.surface.surface_attributes))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surface_parentsurface_surfaceattributes_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Surfacecollection(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            print(len(var.surface.parent_collection))
            print(next(iter(var.surface.parent_collection)))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfacecollection_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteIsundefFalse(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Returns False if it's a valid value, i.e, not NAN
            #[1,1]== 0 is a valid number
            print(var.is_undef_value(var.all().as_array()[1,1]))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_isundef_false_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteChunk(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            ok = True
            chunk_0 = var.chunk((4,5), (4, 5))
            data = chunk_0.as_array().flat
            data_vec = [v for v in data]
            if 4 != len(data_vec):
                ok = False
                print("4 != len(data_vec)")
            if [int(v) for v in data_vec] != [0, 0, 0, 0]:
                ok = False
                print("[int(v) for v in data_vec] != [0, 0, 0,0]")
            chunk_1 = var.chunk((4,4), (4,4))
            chunk_1.set(42)
            chunk_2 = var.chunk((4,5), (4, 5))
            new_data_vec = [int(v) for v in chunk_2.as_array().flat]
            if [int(v) for v in new_data_vec] != [42, 0, 0, 0]:
                ok = False
                print("[int(v) for v in new_data_vec] != [42, 0, 0, 0]")
                print([int(v) for v in new_data_vec])
            chunk_1.set(0)
            print(ok)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_chunk_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteDiscretecodes(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #prints the Discrete codes and values
            print(var.discrete_codes)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_discretecodes_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteDiscretecodeschange(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Change the Discrete code. Change is not persistent and Petrel object is not affected
            original_value = var.discrete_codes[1]
            var.discrete_codes[1] = "Sand sand"
            print(var.discrete_codes)
            
            # Reset values
            var.discrete_codes[1] = original_value
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_discretecodeschange_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteHassameparent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        var_1 = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var_1.readonly = False
        try:
            #Ture is both properties have same Parent
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_hassameparent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteHassameparentValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        var_1 = petrellink._get_seismic_cube('Input/Seismic/Ardmore/Seismic3D')
        var_1.readonly = False
        try:
            #ValueError is throwm if Discrete Surface property is compared with Seismic 3D
            print(var.has_same_parent(var_1))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_hassameparent_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteIsundefTrue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Returns True if the value is NAN
            #First manually set the value to NAN and then do the is_undef
            
            layer = var.all().as_array()
            original_value = layer[0,0]
            layer[0,0] = var.undef_value
            var.all().set(layer)
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            # Reset value
            layer[0,0] = original_value
            var.all().set(layer)
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_isundef_true_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurface(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Prints the parent surface Petrel name
            print(var.surface.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurface_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurfaceextent(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #prints the maximum i & j indices. k will always be zero
            print(var.surface.extent)
            print(var.surface.extent.i)
            print(var.surface.extent.j)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurfaceextent_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurfaceindices(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #prints the indices of the cell at the given (x,y) location
            print(var.surface.indices(484155, 6224170))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurfaceindices_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurfaceindicesValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when (x,y) is outside the Surface
            print(var.surface.indices(400, 600))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurfaceindices_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurfaceposition(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Prints the (x,y,z) position of the cell at the given (i,j).
            print(var.surface.position(32,25))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurfaceposition_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteParentsurfacepositionValueerror(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #ValueError is thrown when (i,j) is outside the Surface geometry
            print(var.surface.position(131,154))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_parentsurfaceposition_valueerror_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscretePetrelname(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Prints the Discrete Surface property Petrel name
            print(var.petrel_name)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_petrelname_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteReadonly(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = True
        try:
            #Cannot write to the property when 'Read only' is checked
            layer = var.all().as_array()
            layer[0,0] = 0
            var.all().set(layer)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_readonly_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteRetrievestats(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            def mylen(d):
                # Can't use built-in len as CPython doesn't know how to the __len__ of a C# Dictionary, although it can iterate over it (using Python.NET)...
                l = 0
                for k in d:
                    l = l + 1
                return l
            
            print(mylen(var.retrieve_stats()) > 0)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_retrievestats_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteSetundefvalue(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #First set the value to 'undef-value', then change it back to a 'def' value
            #For Discrete Surface 'undef_value' = 2417483647 (MAXINT)
            
            layer = var.all().as_array()
            original_value = layer[0, 0]
            layer[0,0] = var.undef_value
            var.all().set(layer)
            print(var.all().as_array()[0,0])
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            layer = var.all().as_array()
            layer[0,0] = -27
            var.all().set(layer)
            print(var.all().as_array()[0,0])
            print(var.is_undef_value(var.all().as_array()[0,0]))
            
            # Reset value
            layer[0, 0] = original_value
            var.all().set(layer)
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_setundefvalue_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteUnitsymbol(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Prints the units for the Discrete Surface property
            print(var.unit_symbol)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_unitsymbol_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteUpdaterawvalues(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            #Can chnage the values when 'Read only' is unchecked
            layer = var.all().as_array()
            original_value = layer[0,0]
            layer[0,0] = 12
            var.all().set(layer)
            print(var.all().as_array()[0,0])
            
            # Reset values
            layer[0,0] = original_value
            var.all().set(layer)
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_updaterawvalues_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributeChunk(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            ok = True
            chunk_0 = var.chunk((4,4), (4, 4))
            data = chunk_0.as_array().flat
            data_vec = [v for v in data]
            if 1 != len(data_vec):
                ok = False
                print("1 != len(data_vec)\n")
            # Or statement because value of changes depending on what petrel tests has been run
            # before.
            if not ([int(v) for v in data_vec] == [-2709] or [int(v) for v in data_vec] == [-2711]):
                ok = False
                print("not ([int(v) for v in data_vec] == [-2709] or [int(v) for v in data_vec] == [-2711]), actually it is {}\n"
                            .format([int(v) for v in data_vec]))
            
            old_value = data_vec[0] 
            chunk_1 = var.chunk((4,4), (4,4))
            chunk_1.set(-3000)
            chunk_2 = var.chunk((4,4), (4, 4))
            new_data_vec = [int(v) for v in chunk_2.as_array().flat]
            if not [int(v) for v in new_data_vec] == [-3000]:
                ok = False
                print("not [int(v) for v in new_data_vec] == [-3000], actually it is {}\n"
                      .format([int(v) for v in new_data_vec]))
            chunk_1.set(old_value)
            print(ok)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattribute_chunk_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogSmoketest(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_global_well_log('Input/Wells/Global well logs/GR')
        var.readonly = True
        try:
            for log in var.logs:
                print (log)
                print (log.well)
                print (len(log.samples))
            
            
            print(var.log('Well_Good'))
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllog_smoketest_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogLog(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_global_well_log('Input/Wells/Global well logs/GR')
        var.readonly = True
        try:
            print(var.log('Well_Good'))
            
            try:
                print(var.log('Well_Goodie'))
            except Exception as exc:
                print(exc)
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllog_log_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogBasic(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_global_well_log('Input/Wells/Global well logs/GR')
        var.readonly = False
        try:
            print(var.petrel_name)
            print(var.unit_symbol)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllog_basic_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogdiscreteLog(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        facies_global = petrellink._get_global_well_log('Input/Wells/Global well logs/Facies', discrete = True)
        facies_global.readonly = False
        try:
            print(facies_global.log('Well_Good'))
            
            try:
                print(facies_global.log('Well_Goodie'))
            except Exception as exc:
                print(exc)
            
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllogdiscrete_log_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogdiscreteLogs(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        facies_global = petrellink._get_global_well_log('Input/Wells/Global well logs/Facies', discrete = True)
        facies_global.readonly = False
        try:
            print("\n".join([v.petrel_name for v in facies_global.logs]))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllogdiscrete_logs_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GlobalwelllogdiscreteWithKey(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        facies_global = petrellink._get_global_well_log('Input/Wells/Global well logs/Facies', discrete = True)
        facies_global.readonly = False
        try:
            print(facies_global.log('Well_Good'))
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\globalwelllogdiscrete_with_key_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
    
    def test_Horizoninterpretation3dCloneOop(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            hi = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
            try:
                hi_clone = hi.clone('Ardmore_clone', copy_values = True)
            except:
                hi_clone = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU_copy/Ardmore_clone')
            
            print(hi.path)
            print(hi_clone.path)
            
            print()
            
            print('** Source **')
            
            print('Extent:', hi.extent)
            print(hi.position(200, 202))
            
            for prop in hi.horizon_property_3ds:
                if prop.petrel_name == "TWT":
                    print()
                    print(prop)
            
                    chunk = prop.chunk((200, 201), (202, 203))
                    vals = chunk.as_array()
                    for i in [0, 1]:
                        for j in [0, 1]:
                            print('%.4f' % vals[i, j], '', end='')
                    print()
                else:
                    print()
                    print(prop)
            
                    prop.readonly = False
                    chunk = prop.chunk((200, 201), (202, 203))
                    with chunk.values() as vals:
                        for i in [0, 1]:
                            for j in [0, 1]:
                                print('%.4f' % vals[i, j], '', end='')
                        print()
            
            print()
            print('** Clone **')
            
            print('Extent:', hi_clone.extent)
            print(hi_clone.position(200, 202))
            
            for prop in hi_clone.horizon_property_3ds:
                if prop.petrel_name == "TWT":
                    print()
                    print(prop)
            
                    chunk = prop.chunk((200, 201), (202, 203))
                    vals = chunk.as_array()
                    for i in [0, 1]:
                        for j in [0, 1]:
                            print('%.4f' % vals[i, j], '', end='')
                    print()
                else:
                    print()
                    print(prop)
            
                    prop.readonly = False
                    chunk = prop.chunk((200, 201), (202, 203))
                    with chunk.values() as vals:
                        for i in [0, 1]:
                            for j in [0, 1]:
                                print('%.4f' % vals[i, j], '', end='')
                        print()
            
            
            try:
                hi_clone = hi.clone('Ardmore_clone_noval', copy_values = False)
            except:
                hi_clone = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU_copy/Ardmore_clone_noval')
            
            print()
            print(hi_clone.path)
            print()
            
            print('** Clone noval**')
            
            print('Extent:', hi_clone.extent)
            print(hi_clone.position(200, 202))
            
            for prop in hi_clone.horizon_property_3ds:
                if prop.petrel_name == "TWT":
                    print()
                    print(prop)
            
                    chunk = prop.chunk((200, 201), (202, 203))
                    vals = chunk.as_array()
                    for i in [0, 1]:
                        for j in [0, 1]:
                            print('%.4f' % vals[i, j], '', end='')
                    print()
                else:
                    print()
                    print(prop)
            
                    prop.readonly = False
                    chunk = prop.chunk((200, 201), (202, 203))
                    with chunk.values() as vals:
                        for i in [0, 1]:
                            for j in [0, 1]:
                                print('%.4f' % vals[i, j], '', end='')
                        print()
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation3D_clone_oop_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WellsurveySetSurveyAsDefinitive(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_explicit_well_survey('Input/Wells/Well_Good/Explicit survey 1')
        var.readonly = False
        var_1 = petrellink._get_xyz_well_survey('Input/Wells/Well_Good/XYZ')
        var_1.readonly = False
        var_2 = petrellink._get_xytvd_well_survey('Input/Wells/Well_Good/XYTVD')
        var_2.readonly = False
        var_3 = petrellink._get_dxdytvd_well_survey('Input/Wells/Well_Good/DXDYTVD')
        var_3.readonly = False
        var_4 = petrellink._get_mdinclazim_well_survey('Input/Wells/Well_Good/MDINCLAZIM')
        var_4.readonly = False
        well = petrellink._get_well('Input/Wells/Well_Good')
        well.readonly = False
        try:
            print(well.retrieve_stats().get('Number of points'))
            
            # var_1 -> XYZ well survey
            var_1.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            var.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            
            # var_2 -> XYTVD well survey
            var_2.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            var.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            
            # var_3 -> DXDYTVD well survey
            var_3.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            var.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            
            # var_4 -> MD incl azim well survey
            var_4.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
            
            # Explicit at the end to not introduce changes into the project
            # var -> Explicit survey
            var.set_survey_as_definitive()
            print(well.retrieve_stats().get('Number of points'))
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\wellsurvey_set_survey_as_definitive_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributeChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/TWT')
        var.readonly = False
        try:
            print(var.readonly)
            
            chunk = var.chunk((5,15),(5,10))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] * 2
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().head())
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
            chunk.set(df_to_reset_values)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattribute_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_SurfaceattributediscreteChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_surface_attribute('Input/TWT Surface/BCU/Facies', discrete = True)
        var.readonly = False
        try:
            print(var.readonly)
            
            chunk = var.chunk((5,15),(5,10))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] + 1
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().head())
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
            #Try set non-integer values -should raise ValueError
            df.loc[:,'Value_new'] = df.loc[:,'Value'] + 1.05
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
            chunk.set(df_to_reset_values)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\surfaceattributediscrete_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizoninterpretation3dChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_horizon_interpretation_3d('Input/Seismic/Interpretation folder 1/BCU/Ardmore')
        var.readonly = False
        try:
            print(var.readonly)
            
            chunk = var.chunk((5,15),(5,10))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] * 2
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().head())
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
            chunk.set(df_to_reset_values)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizoninterpretation3D_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_Horizonproperty3dChunkSetDf(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            var = petrellink.horizon_properties['Input/Seismic/Interpretation folder 1/BCU/Ardmore/Autotracker: Confidence']
            var.readonly = False
            print(var.readonly)
            
            chunk = var.chunk((5,15),(5,10))
            df_to_reset_values = chunk.as_dataframe()
            
            df = chunk.as_dataframe()
            df['Value_new'] = df['Value']
            df.loc[:,'Value_new'] = df.loc[:,'Value'] * 2
            
            #set with df - correct input
            try:
                chunk.set(df)
            except Exception as err:
                print(err)
            print(chunk.as_dataframe().head())
            try:
                chunk.set(df, 'Value_new')
            except Exception as err:
                print(err)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
            chunk.set(df_to_reset_values)
            print(var.chunk((5,15),(5,10)).as_dataframe().head())
            
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\horizonproperty3D_chunk_set_df_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyChunkSize(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Rho')
        var.readonly = False
        try:
            c = var.chunk((10, 20), (10, 20), (10, 20))
            assert c.as_array().shape == (11, 11, 11)
            print('ok')
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_chunk_size_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_GridpropertyChunkSize1(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        var = petrellink._get_grid_property('Models/Structural grids/Model_Good/Properties/Facies', discrete = True)
        var.readonly = False
        try:
            c = var.chunk((10, 20), (10, 20), (10, 20))
            assert c.as_array().shape == (11, 11, 11)
            print('ok')
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\gridproperty_chunk_size_1_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))




    
    def test_WellLogExceptions(self, petrellink):
        try_output = io.StringIO()
        sys_out = sys.stdout
        sys.stdout = try_output
        is_oop = True
        
        try:
            from cegalprizm.pythontool.exceptions import UserErrorException
            
            dt = petrellink.well_logs['Input/Wells/Well_Good/Well logs/DT']
            facies = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies']
            
            facies.readonly = False
            
            dt.readonly = False
            mds = [5700, 5700.1, 5700.2]
            values = [-10.0, 1]
            values_disc = [6.99, 4]
            
            failed = False
            
            try:
                dt.readonly = False
                dt.set_values(mds, values)
            except ValueError as ve:
                if not "mds and values must be the same length" in str(ve):
                    failed |= True
            except:
                failed |= True
            
            try:
                facies.readonly = False
                facies.set_values(mds, values)
            except ValueError as ve:
                if not "mds and values must be the same length" in str(ve):
                    failed |= True
            except:
                failed |= True
            
            mds = dt.as_dataframe()['MD'].to_list()
            values = dt.as_dataframe()['Value'].to_list()
            mds.append(10000)
            values.append(150)
            mds.append(1000)
            values.append(200)
            try:
                dt.readonly = False
                dt.set_values(mds, values) #Here petrellink dies
            except UserErrorException as ve:
                if not "Measured depths are not strictly monotonic" in str(ve):
                    failed |= True
            except:
                failed |= True
            if failed:
                print("Failed")
            else:
                print("All good")
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
        with open(r'..\..\Blueback.PythonTool.PythonApi.PetrelTest\Resources\ValidatedScripts\txt\well_log_exceptions_expected.txt', 'r') as f:
            expected_output =  f.read().strip()
        try_output.seek(0)
        actual_output = try_output.read().strip()
        sys.stdout = sys_out
        print('')
        print('##### expected_output:')
        print(expected_output)
        print('##### actual_output:')
        print(actual_output)
        assert ''.join(expected_output.split()) in ''.join(actual_output.split()), "\nexpected:\n%s\n\nactual:\n%s\n\n" %(''.join(expected_output.split()), ''.join(actual_output.split()))
