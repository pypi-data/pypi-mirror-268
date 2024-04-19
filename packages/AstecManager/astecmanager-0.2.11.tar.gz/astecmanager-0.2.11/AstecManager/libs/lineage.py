from AstecManager.libs.data import get_longid,get_id_t,Cell
import xml.etree.ElementTree as ET
import os
import numpy as np
from AstecManager.libs.ioproperties import read_dictionary

def indent_xml(elem, level=0):
    """

    :param elem: 
    :param level:  (Default value = 0)

    """
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent_xml(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

def SaveTabToXMLInfo(path_input,path_output,tab,node_name):
    """

    :param path_input: 
    :param path_output: 
    :param tab: 
    :param node_name: 

    """
    source = open(path_input)
    tree = ET.parse(source)
    tree = tree.getroot()
    selec_node = node_name
    name_selec_elem = tree.find(selec_node)
    if name_selec_elem is None:
        name_selec_elem = ET.SubElement(tree, selec_node)
    for cell in name_selec_elem.findall('cell'):
        if int(cell.get('cell-id')) in tab.keys() or cell.get(
                'cell-id') in tab.keys() and tab is not None and tab[cell.get('cell-id')] is not None:
            cell.text =str(tab[cell.get('cell-id')])
            tab.pop(cell.get('cell-id'), None)
    for cell in tab:
        new_cell = ET.SubElement(name_selec_elem, 'cell')
        new_cell.set('cell-id', cell)
        new_cell.text = str(tab[cell])
    indent_xml(tree)
    source.close()
    mydata = ET.tostring(tree, encoding='utf8', method='xml').decode("utf8")
    myfile = open(path_output, "w+")
    myfile.write(mydata)
    myfile.close()


def AddNodeToXML(xml_file, value_dict, node_name,node_subname,identifier_text='value'):
    """

    :param xml_file: 
    :param value_dict: 
    :param node_name: 
    :param node_subname: 
    :param identifier_text:  (Default value = 'value')

    """
    print(str(xml_file))
    if not os.path.isfile(xml_file) or os.stat(xml_file).st_size == 0:
        print("XML file not found , create it with path : "+str(xml_file))
        f = open(xml_file,"w+")
        f.close()
        root = ET.Element('root')
        tree = ET.ElementTree(root)
        tree.write(xml_file)
    source = open(xml_file)
    tree = ET.parse(source)
    tree = tree.getroot()
    selec_node = node_name
    name_selec_elem = tree.find(selec_node)
    if name_selec_elem is None:
        name_selec_elem = ET.SubElement(tree, selec_node)
    for cell in name_selec_elem.findall(node_subname):
        if cell.get(identifier_text) in value_dict.keys() or cell.get(
                identifier_text) in value_dict.keys() and value_dict is not None and value_dict[cell.get(identifier_text)] is not None:
            cell.text =str(value_dict[cell.get(identifier_text)])
            value_dict.pop(cell.get(identifier_text), None)
    for cell in value_dict:
        new_cell = ET.SubElement(name_selec_elem, node_subname)
        if cell != "":
            new_cell.set(identifier_text, str(cell))
        new_cell.text = str(value_dict[cell])
    indent_xml(tree)
    source.close()
    mydata = ET.tostring(tree, encoding='utf8', method='xml').decode("utf8")
    myfile = open(xml_file, "w+")
    myfile.write(mydata)
    myfile.close()

def SaveTabToTxtInfo(path_output,name_file,tab, time_string,type="selection"):
    """

    :param path_output: 
    :param name_file: 
    :param tab: 
    :param time_string: 

    """
    if not os.path.isdir(path_output):
        os.mkdir(path_output)
    f = open(os.path.join(path_output,name_file), "w+")
    f.write("#Information that matches names with a selection" + "\n")
    f.write("#Generated on : " + time_string + "\n")
    f.write("type:"+str(type)+"\n")
    for idc in tab:
        t, ida = get_id_t(idc)
        line = str(t) + "," + str(ida) + ",0:" + str(tab[idc]) + "\n"
        f.write(line)
    f.close()


def LoadCellList(path_lineage):
    """

    :param path_lineage: 

    """
    try:
        source = open(path_lineage)
    except:
        return None
    tree = ET.parse(source)
    cell_list_g = {}
    tree = tree.getroot()
    lineage_elem = tree.find('cell_lineage')
    if lineage_elem is not None:
        for cell in lineage_elem.findall('cell'):
            cell_t,cell_id = get_id_t(cell.get('cell-id').replace("'","").replace('[','').replace(']','').replace(" ",""))
            cell_key = str(get_longid(cell_t,cell_id))
             #cell_key = str(cell_t)+","+str(cell_id)
            if not cell_key in cell_list_g:
                cell_object = Cell(int(cell_id),int(cell_t))
                cell_list_g[cell_key] = cell_object
            cell_childs = cell.text.split(',')
            for cell_child_in_list in cell_childs:
                cell_child_t,cell_child_id = get_id_t(cell_child_in_list.replace("'","").replace('[','').replace(']','').replace(" ",""))
                cell_child_key = str(get_longid(cell_child_t,cell_child_id))
                if not cell_child_key in cell_list_g:
                    cell_child_object = Cell(int(cell_child_id), int(cell_child_t))
                    cell_list_g[cell_child_key] = cell_child_object

                if not cell_list_g[cell_child_key] in cell_list_g[cell_key].daughters:
                    cell_list_g[cell_child_key].add_mother(cell_list_g[cell_key])
        return cell_list_g
    return None

def list_ids_by_time(lineage):
    """

    :param lineage: 

    """
    ids = {}
    local_list = LoadCellList(lineage)
    for cell in local_list:
        tc,idc=get_id_t(cell)
        if not tc in ids:
            ids[tc] = [idc]
        else :
            ids[tc].append(idc)
    return ids


def GetCellLifetime(cell):
    """

    :param cell: 

    """
    list_cells = [cell,]
    daughters = GetCellLifeFutur(cell)
    mothers = GetCellLifePast(cell)
    for dau in daughters:
        if not dau in list_cells:
            list_cells.append(dau)
    for mot in mothers:
        if not mot in list_cells:
            list_cells.append(mot)
    #print("cell : "+str(cell))
    #print("Cells found : "+str(len(list_cells)))
    return list_cells

def GetCellWholeLifetime(cell):
    """

    :param cell:

    """
    list_cells = [cell,]
    daughters = GetAllCellLifeFutur(cell)
    mothers = GetCellAllLifePast(cell)
    for dau in daughters:
        if not dau in list_cells:
            list_cells.append(dau)
    for mot in mothers:
        if not mot in list_cells:
            list_cells.append(mot)
    #print("cell : "+str(cell))
    #print("Cells found : "+str(len(list_cells)))
    return list_cells


def GetAllCellLifeFutur(cell):
    """

    :param cell:

    """
    list_cells = []
    if cell is None or cell.daughters is None or len(cell.daughters) < 1:
        #print("Futur : cell is : "+str(cell))
        #print("Futur : cell has no daughters")
        return list_cells
    for daughter in cell.daughters:
        cells = GetAllCellLifeFutur(daughter)
        for cell_child in cells:
            list_cells.append(cell_child)

    #print("number of daughters found : "+str(len(cells)))
    if list_cells is not None:
        list_cells.append(cell)
    return list_cells

def GetCellAllLifePast(cell):
    """

    :param cell:

    """
    list_cells = []
    #if cell is not None and cell.mothers is not None:
    #    print(cell.mothers)
    if cell is None or cell.mothers is None or len(cell.mothers) == 0 or cell.mothers[0].daughters is None:
        #print("Past : cell is : "+str(cell))
        #print("Past : cell has no mothers")
        return list_cells
    for mother in cell.mothers:
        cells =GetCellAllLifePast(mother)
        for cell_child in cells:
            list_cells.append(cell_child)
    #print("number of mothers found : "+str(len(cells)))
    if list_cells is not None:
        list_cells.append(cell)
    return list_cells

def GetCellLifeFutur(cell):
    """

    :param cell: 

    """
    list_cells = [cell,]
    if cell is None or cell.daughters is None or len(cell.daughters) != 1:
        #print("Futur : cell is : "+str(cell))
        #print("Futur : cell has no daughters")
        return list_cells
    cells = GetCellLifeFutur(cell.daughters[0])
    #print("number of daughters found : "+str(len(cells)))
    if cells is not None:
        cells.append(cell)
    return cells

def GetCellLifePast(cell):
    """

    :param cell: 

    """
    list_cells = [cell,]
    #if cell is not None and cell.mothers is not None:
    #    print(cell.mothers)
    if cell is None or cell.mothers is None or len(cell.mothers) == 0 or cell.mothers[0].daughters is None or len(cell.mothers[0].daughters) != 1:
        #print("Past : cell is : "+str(cell))
        #print("Past : cell has no mothers")
        return list_cells
    cells =GetCellLifePast(cell.mothers[0])
    #print("number of mothers found : "+str(len(cells)))
    if cells is not None:
        cells.append(cell)
    return cells

def GetCellLifePastnodeath(cell):
    """

    :param cell: 

    """
    list_cells = [cell,]
    #if cell is not None and cell.mothers is not None:
    #    print(cell.mothers)
    if cell is None or cell.mothers is None or len(cell.mothers) == 0 or cell.mothers[0].daughters is None or len(cell.mothers[0].daughters) != 1:
        #print("Past : cell is : "+str(cell))
        #print("Past : cell has no mothers")
        return list_cells
    cells =GetCellLifePastnodeath(cell.mothers[0])
    #print("number of mothers found : "+str(len(cells)))
    if cells is not None:
        cells.append(cell)
    return cells



def Get_Cell_Names(path_lineage, info="cell_name"):
    """

    :param path_lineage: 
    :param info:  (Default value = "cell_name")

    """
    cell_values={}
    source = open(path_lineage)
    tree = ET.parse(source)
    tree = tree.getroot()
    lineage_elem = tree.find(info)
    if lineage_elem is not None:
        for cell in lineage_elem.findall('cell'):
            cell_id = cell.get('cell-id')
            cell_child = cell.text
            if cell_child is not None and cell_child != "None":
                new_val = str(cell_child.replace("'", "").replace(" ", ""))
                cell_values[cell_id] = new_val
        # print(str(result))
        return cell_values
    return None

def Get_Cell_Names_Swapped(path_lineage, info="cell_name"):
    """

    :param path_lineage: 
    :param info:  (Default value = "cell_name")

    """
    cell_values={}
    source = open(path_lineage)
    tree = ET.parse(source)
    tree = tree.getroot()
    lineage_elem = tree.find(info)
    if lineage_elem is not None:
        for cell in lineage_elem.findall('cell'):
            cell_id = cell.get('cell-id')
            cell_child = cell.text
            if cell_child is not None and cell_child != "None":
                new_val = str(cell_child.replace("'", "").replace(" ", ""))
                if not new_val in cell_values:
                    cell_values[new_val] = []
                cell_values[new_val].append(cell_id)
        # print(str(result))
        return cell_values
    return None

def Get_Cell_Contact_Surface(path_lineage, info="cell_contact_surface"):
    """

    :param path_lineage: 
    :param info:  (Default value = "cell_contact_surface")

    """
    cell_values={}
    source = open(path_lineage)
    tree = ET.parse(source)
    tree = tree.getroot()
    lineage_elem = tree.find(info)
    if lineage_elem is not None:
        for cell in lineage_elem.findall('cell'):
            cell_id = cell.get('cell-id')
            cell_child = cell.text
            if cell_child is not None and cell_child != "None":
                new_val = str(cell_child.replace("'", "").replace(" ", ""))
                cell_values[cell_id] = new_val
        # print(str(result))
        return cell_values
    return None

def Get_Cell_Values_Float(path_lineage, info, filter_background=False):
    """

    :param path_lineage: 
    :param info: 
    :param filter_background:  (Default value = False)

    """
    cell_values = {}
    min_val = 1000000000
    max_val = -1000000000
    source = open(path_lineage)
    tree = ET.parse(source)
    tree = tree.getroot()
    lineage_elem = tree.find(info)
    if lineage_elem is not None:
        for cell in lineage_elem.findall('cell'):
            cell_id = cell.get('cell-id')
            ct, cid = get_id_t(cell_id)
            if not filter_background or cid != 1:
                cell_child = cell.text
                if cell_child is not None and cell_child != "None":
                    new_val = float(cell_child.replace("'", "").replace(" ", ""))
                    if new_val > max_val:
                        max_val = new_val
                    if new_val < min_val:
                        min_val = new_val
                    cell_values[cell_id] = new_val
        # print(str(result))
        return min_val, max_val, cell_values
    return 0, 0, None


def _find_t(cells_per_time, n):
    """

    :param cells_per_time: 
    :param n: 

    """
    if n in cells_per_time.values():
        times = [t for t in cells_per_time if cells_per_time[t] == n]
        return (min(times) + max(times))/2.0
    smaller_times = [t for t in cells_per_time if cells_per_time[t] < n]
    larger_times = [t for t in cells_per_time if cells_per_time[t] > n]
    ts = max(smaller_times)
    tl = min(larger_times)
    return ts + (tl - ts) * (n - cells_per_time[ts]) / (cells_per_time[tl] - cells_per_time[ts])


def _temporal_alignement(ref_cells_per_time, cells_per_time):
    """

    :param ref_cells_per_time: 
    :param cells_per_time: 

    """
    first = max(min(ref_cells_per_time.values()), min(cells_per_time.values()))
    last = min(max(ref_cells_per_time.values()), max(cells_per_time.values()))
    ref_times = []
    times = []
    for n in range(first, last+1):
        if n not in ref_cells_per_time.values() and n not in cells_per_time.values():
            continue
        ref_times += [_find_t(ref_cells_per_time, n)]
        times += [_find_t(cells_per_time, n)]
    num = sum(np.multiply(times, ref_times)) - sum(times) * sum(ref_times) / len(times)
    den = sum(np.multiply(times, times)) - sum(times) * sum(times) / len(times)
    a = num/den
    b = (sum(ref_times) - a * sum(times)) / len(times)
    return a, b



def temporal_alignment(ref_lineage, lineage, ref_time_digits_for_cell_id=4, time_digits_for_cell_id=4):
    """

    :param ref_lineage: 
    :type ref_lineage: reference lineage
    :param lineage: 
    :type lineage: lineage to be aligned with the reference lineage
    :param time_digits_for_cell_id:  (Default value = 4)
    :type time_digits_for_cell_id: number of digits for the cell number in the unique cell identifier
    :param ref_time_digits_for_cell_id:  (Default value = 4)

    
    """
    ref_div = 10 ** ref_time_digits_for_cell_id
    div = 10 ** time_digits_for_cell_id

    ref_lineage_o = read_dictionary(ref_lineage)["cell_lineage"]
    cells = list(set(ref_lineage_o.keys()).union(set([v for values in list(ref_lineage_o.values()) for v in values])))
    cells = sorted(cells)
    ref_cells_per_time = {}
    for c in cells:
        t = int(c) // ref_div
        ref_cells_per_time[t] = ref_cells_per_time.get(t, 0) + 1
    lineage_o = read_dictionary(lineage)["cell_lineage"]
    cells = list(set(lineage_o.keys()).union(set([v for values in list(lineage_o.values()) for v in values])))
    cells = sorted(cells)
    cells_per_time = {}
    for c in cells:
        t = int(c) // div
        cells_per_time[t] = cells_per_time.get(t, 0) + 1

    return _temporal_alignement(ref_cells_per_time, cells_per_time)

def get_aligned_time(t,a,b):
    """

    :param t: 
    :param a: 
    :param b: 

    """
    return int((a*t)+b)

            
def count_cells(lineage_input_path,cell_list=None,remove_time=[],only_times=[]):
    """

    :param lineage_input_path: 
    :param cell_list:  (Default value = None)
    :param remove_time:  (Default value = [])
    :param only_times:  (Default value = [])

    """
    cell_count_by_time = {}
    local_list = cell_list
    if local_list is None:
        local_list = LoadCellList(lineage_input_path)
    for cell_key in local_list:
        cell_obj = local_list[cell_key]
        if not cell_obj.t in remove_time and (only_times==[] or cell_obj.t in only_times):
            if not cell_obj.t in cell_count_by_time:
                cell_count_by_time[cell_obj.t] = 0
            cell_count_by_time[cell_obj.t] += 1
    return dict(sorted(cell_count_by_time.items()))


def get_t_start_objs(start_time,cell_list):
    """

    :param start_time: 
    :param cell_list: 

    """
    obj_list = []
    for cell in cell_list:
        cell_t,cell_id = get_id_t(str(cell))
        if cell_t == start_time:
            obj_list.append(cell_list[cell])
    return obj_list

def get_min_timepoint_leaf(cellobj):
    """

    :param cellobj: 

    """
    minc = 100000000
    if cellobj.daughters is None or len(cellobj.daughters) <1:
        return cellobj.t
    if len(cellobj.daughters) == 1:
        return get_min_timepoint_leaf(cellobj.daughters[0])
    else:
        for daughter in cellobj.daughters:
            minc = min(minc,get_min_timepoint_leaf(daughter))
    return minc

def get_max_timepoint_leaf(cellobj):
    """

    :param cellobj: 

    """
    maxc = -100000000
    if cellobj.daughters is None or len(cellobj.daughters) <1:
        return cellobj.t
    if len(cellobj.daughters) == 1:
        return get_max_timepoint_leaf(cellobj.daughters[0])
    else:
        for daughter in cellobj.daughters:
            maxc = max(maxc,get_max_timepoint_leaf(daughter))
    return maxc

def get_timepoint_leaf(cellobj):
    """

    :param cellobj: 

    """
    result = []
    cells_leaves=[]
    if cellobj.daughters is None or len(cellobj.daughters) <1:
        return [str(get_longid(cellobj.t,cellobj.id))],[cellobj.t]
    if len(cellobj.daughters) == 1:
        return get_timepoint_leaf(cellobj.daughters[0])
    else:
        for daughter in cellobj.daughters:
            cells_leaves_c,leaveschildren = get_timepoint_leaf(daughter)
            for leaves in leaveschildren:
                result.append(leaves)
            for celll in cells_leaves_c:
                cells_leaves.append(celll)
    return cells_leaves,result

def build_all_leaves(lineage_input_path,start_time,end_time,cell_list=None):
    """

    :param lineage_input_path: 
    :param start_time: 
    :param end_time: 
    :param cell_list:  (Default value = None)

    """
    all_leaves=[]
    mars_ids = []
    cells_ids = []
    total_leaves_count = 0
    early_death_count = 0
    local_list = cell_list
    if local_list is None:
        local_list = LoadCellList(lineage_input_path)
    obj_list = get_t_start_objs(start_time,local_list)
    for objcell in obj_list:
        cellsleaf,leaves = get_timepoint_leaf(objcell)
        found_early_leave = False
        for i in range(0,len(leaves)):
            total_leaves_count += 1
            if int(leaves[i]) != int(end_time):
                early_death_count += 1
                found_early_leave = True
                cells_ids.append(str(cellsleaf[i]))
        if found_early_leave:
            all_leaves.append(leaves)
            mars_ids.append(str(get_longid(objcell.t,objcell.id)))
    final_proportion = 0
    if total_leaves_count > 0:
        final_proportion = (early_death_count/total_leaves_count)*100
    return cells_ids,final_proportion,mars_ids,all_leaves



def find_ids_at_end(current_cell,end_time):
    """

    :param current_cell: 
    :param end_time: 

    """
    result = []
    if current_cell.t == end_time:
        result.append(current_cell.id)
        return result
    if current_cell is None or current_cell.daughters is None or len(current_cell.daughters) ==0 or current_cell.t > end_time:
        return result
    if len(current_cell.daughters)==1:
        temp_r = find_ids_at_end(current_cell.daughters[0],end_time)
        for cell in temp_r:
            result.append(cell)
    else:
        for cell_d in current_cell.daughters:
            temp_r = find_ids_at_end(cell_d,end_time)
            for cell in temp_r:
                result.append(cell)
    return result

