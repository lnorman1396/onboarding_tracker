#-------------------------------------------------------IMPORTS-----------------------------------------------------------------#
import sqlite3
#-------------------------------------------------------ESTABLISH__CONNECTION-----------------------------------------------------------------#
# Establish Connection
#Ensure threadding set to false 
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()
#-------------------------------------------------------CREATE__TABLES-----------------------------------------------------------------#
# main Table
# depot, info, scheduler_name, se_name, main_dt
def create_main_table():
    cr_main_table_str = "CREATE TABLE IF NOT EXISTS main_table(depot TEXT, info TEXT, scheduler_name TEXT, se_name TEXT, main_DT TEXT)"
    c.execute(cr_main_table_str)

def create_select_table():
    cr_select_table_str = "CREATE TABLE IF NOT EXISTS select_table(select_1a TEXT, select_1b)"
    c.execute(cr_select_table_str)

# Pre-Requesites
# pre_HM, pre_dh, pre_eo, pre_info, pre_DT
def create_pre_table():
    cr_pre_table_str = "CREATE TABLE IF NOT EXISTS pre_table(depot TEXT, pre_HM TEXT, pre_dh TEXT, pre_eo TEXT, pre_info TEXT, pre_DT TEXT, pre_metric INT, pre_val TEXT, pre_HM_text TEXT, pre_dh_text TEXT, pre_HM_diff INT, pre_dh_diff INT, pre_eo_diff INT, pre_eo_text TEXT)"
    c.execute(cr_pre_table_str)

# Vehicle_Logistics
#   vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info ,vl_DT
def create_vl_table():
    cr_vl_table_str = "CREATE TABLE IF NOT EXISTS vl_table(depot TEXT, vl_algo TEXT, vl_cost TEXT, vl_dep_set TEXT, vl_dead_cat TEXT, vl_mid_park TEXT, vl_pre_tr TEXT, vl_info TEXT, vl_DT TEXT, vl_metric INT)"
    c.execute(cr_vl_table_str)

#Duty Logistics
#   dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info, dl_DT
def create_dl_table():
    cr_dl_table_str = "CREATE TABLE IF NOT EXISTS dl_table(depot TEXT, dl_travel TEXT , dl_pref_gr TEXT, dl_spl_br TEXT, dl_duty_breaks TEXT, dl_info TEXT, dl_DT TEXT, dl_metric INT)"
    c.execute(cr_dl_table_str)

# Piece Cutting
#   pc_rel_pt, pc_rel_tm, pc_short_pc, pc_cust_du_pr, pc_info, pc_DT
def create_pc_table():
    cr_pc_table_str = "CREATE TABLE IF NOT EXISTS pc_table(depot TEXT, pc_rel_pt TEXT, pc_rel_tm TEXT, pc_short_pc TEXT, pc_cust_du_pr TEXT, pc_info TEXT, pc_DT TEXT)"
    c.execute(cr_pc_table_str)

# Duty Characteristics
#   dc_pref_route, dc_driv_ba, dc_change_veh, dc_time_def, dc_break_pref, dc_driv_sign, dc_time_lim, dc_duty_types, dc_duty_id_gen, dc_info, dc_DT
def create_dc_table():
    cr_dc_table_str = "CREATE TABLE IF NOT EXISTS dc_table(DEPOT TEXT, dc_pref_route TEXT, dc_driv_ba TEXT, dc_change_veh TEXT, dc_time_def TEXT, dc_break_pref TEXT, dc_driv_sign TEXT, dc_time_lim TEXT, dc_duty_types TEXT, dc_duty_id_gen TEXT, dc_info TEXT, dc_DT TEXT)"
    c.execute(cr_dc_table_str)

# Benchmark
#   be_wk_duty_sum_comp, be_implement_sat_prefs, be_sat_duty_sum_comp, be_implement_sun_prefs, be_sun_duty_sum_comp, be_benchmark_sign_off, be_info, be_DT
def create_be_table():
    cr_be_table_str = "CREATE TABLE IF NOT EXISTS be_table(depot TEXT, be_wk_duty_sum_comp TEXT, be_implement_sat_prefs TEXT, be_sat_duty_sum_comp TEXT, be_implement_sun_prefs TEXT, be_sun_duty_sum_comp TEXT, be_benchmark_sign_off TEXT, be_info TEXT, be_DT TEXT)"
    c.execute(cr_be_table_str)

# Preoptimisation
#   po_be_rule_vio, po_global_con, po_lock_duty, po_info, po_DT
def create_po_table():
    cr_po_table_str = "CREATE TABLE IF NOT EXISTS po_table(depot TEXT, po_be_rule_vio TEXT, po_global_con TEXT, po_lock_duty TEXT, po_info TEXT, po_DT TEXT)"
    c.execute(cr_po_table_str)

# Optimisation
#   op_wk, op_wk_valid, op_sat, op_sat_valid, op_sun, op_sun_valid, op_signoff, op_info, op_DT
def create_op_table():
    cr_op_table_str = "CREATE TABLE IF NOT EXISTS op_table(depot TEXT, op_wk TEXT, op_wk_valid TEXT, op_sat TEXT, op_sat_valid TEXT, op_sun TEXT, op_sun_valid TEXT, op_signoff TEXT, op_info TEXT, op_DT TEXT)"
    c.execute(cr_op_table_str)


#-------------------------------------------------------ADD_DATA_TO_TABLES-----------------------------------------------------------------#
#Add data to main table
def add_data_to_main_table(depot, info, scheduler_name, se_name, main_dt):
    add_data_main_str = 'INSERT INTO main_table(depot, info, scheduler_name, se_name, main_dt) VALUES (?,?,?,?,?)'
    c.execute(add_data_main_str, (depot, info, scheduler_name, se_name, main_dt))
    conn.commit()

def add_data_to_select_table(select_1a, select_1b):
    add_data_select_str = 'INSERT INTO select_table(select_1a, select_1b) VALUES (?,?)'
    c.execute(add_data_select_str, (select_1a, select_1b))
    conn.commit()


#Add data to pre_table
def add_data_to_pre_table(depot, pre_HM, pre_dh, pre_eo, pre_info, pre_DT, pre_metric, pre_val, pre_HM_text, pre_dh_text, pre_HM_diff, pre_dh_diff, pre_eo_diff, pre_eo_text):
    add_data_pre_str = 'INSERT INTO pre_table(depot,pre_HM, pre_dh, pre_eo, pre_info, pre_DT, pre_metric, pre_val, pre_HM_text, pre_dh_text, pre_HM_diff, pre_dh_diff, pre_eo_diff, pre_eo_text) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    c.execute(add_data_pre_str, (depot, pre_HM, pre_dh, pre_eo, pre_info, pre_DT, pre_metric, pre_val, pre_HM_text, pre_dh_text, pre_HM_diff, pre_dh_diff, pre_eo_diff, pre_eo_text))
    conn.commit()
#Add data to vl_table


def add_data_to_vl_table(depot, vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info ,vl_DT, vl_metric):
    add_data_vl_str = 'INSERT INTO vl_table(depot, vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info ,vl_DT, vl_metric) VALUES (?,?,?,?,?,?,?,?,?,?)'
    c.execute(add_data_vl_str, (depot, vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info ,vl_DT, vl_metric))
    conn.commit()
#Add data to dl_table
def add_data_to_dl_table(depot, dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info, dl_DT, dl_metric):
    add_data_dl_str = 'INSERT INTO dl_table(depot, dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info, dl_DT, dl_metric) VALUES (?,?,?,?,?,?,?,?)'
    c.execute(add_data_dl_str, (depot, dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info, dl_DT, dl_metric))
    conn.commit()
#Add data to pc_table
def add_data_to_pc_table(depot, pc_rel_pt, pc_rel_tm, pc_short_pc, pc_cust_du_pr, pc_info, pc_DT):
    add_data_pc_str = 'INSERT INTO pc_table(depot, pc_rel_pt, pc_rel_tm, pc_short_pc, pc_cust_du_pr, pc_info, pc_DT) VALUES (?,?,?,?,?,?,?)'
    c.execute(add_data_pc_str, (depot, pc_rel_pt, pc_rel_tm, pc_short_pc, pc_cust_du_pr, pc_info, pc_DT))
    conn.commit()
#Add data to dc_table
def add_data_to_dc_table(depot, dc_pref_route, dc_driv_ba, dc_change_veh, dc_time_def, dc_break_pref, dc_driv_sign, dc_time_lim, dc_duty_types, dc_duty_id_gen, dc_info, dc_DT):
    add_data_dc_str = 'INSERT INTO dc_table(depot, dc_pref_route, dc_driv_ba, dc_change_veh, dc_time_def, dc_break_pref, dc_driv_sign, dc_time_lim, dc_duty_types, dc_duty_id_gen, dc_info, dc_DT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
    c.execute(add_data_dc_str, (depot, dc_pref_route, dc_driv_ba, dc_change_veh, dc_time_def, dc_break_pref, dc_driv_sign, dc_time_lim, dc_duty_types, dc_duty_id_gen, dc_info, dc_DT))
    conn.commit()
#Add data to be_table
def add_data_to_be_table(depot, be_wk_duty_sum_comp, be_implement_sat_prefs, be_sat_duty_sum_comp, be_implement_sun_prefs, be_sun_duty_sum_comp, be_benchmark_sign_off, be_info, be_DT):
    add_data_be_str = 'INSERT INTO be_table(depot, be_wk_duty_sum_comp, be_implement_sat_prefs, be_sat_duty_sum_comp, be_implement_sun_prefs, be_sun_duty_sum_comp, be_benchmark_sign_off, be_info, be_DT) VALUES (?,?,?,?,?,?,?,?,?)'
    c.execute(add_data_be_str, (depot, be_wk_duty_sum_comp, be_implement_sat_prefs, be_sat_duty_sum_comp, be_implement_sun_prefs, be_sun_duty_sum_comp, be_benchmark_sign_off, be_info, be_DT))
    conn.commit()
#Add data to po_table
def add_data_to_po_table(depot, po_be_rule_vio, po_global_con, po_lock_duty, po_info, po_DT):
    add_data_po_str = 'INSERT INTO po_table(depot, po_be_rule_vio, po_global_con, po_lock_duty, po_info, po_DT) VALUES (?,?,?,?,?,?)'
    c.execute(add_data_po_str, (depot, po_be_rule_vio, po_global_con, po_lock_duty, po_info, po_DT))
    conn.commit()
#Add data to op_table
def add_data_to_op_table(depot, op_wk, op_wk_valid, op_sat, op_sat_valid, op_sun, op_sun_valid, op_signoff, op_info, op_DT):
    add_data_op_str = 'INSERT INTO op_table(depot, op_wk, op_wk_valid, op_sat, op_sat_valid, op_sun, op_sun_valid, op_signoff, op_info, op_DT) VALUES (?,?,?,?,?,?,?,?,?,?)'
    c.execute(add_data_op_str, (depot, op_wk, op_wk_valid, op_sat, op_sat_valid, op_sun, op_sun_valid, op_signoff, op_info, op_DT))
    conn.commit()


#-----------------------------------------------------VIEW_DATA_FROM_TABLES-----------------------------------------------------------------#
#View data to main_table
def view_data_to_main_table():
    view_data_main_str = 'SELECT * FROM main_table'
    c.execute(view_data_main_str)
    data = c.fetchall()
    return data

def view_data_to_select_table():
    view_data_select_str = 'SELECT * FROM select_table'
    c.execute(view_data_select_str)
    data = c.fetchall()
    return data

#view data to pre_table
def view_data_to_pre_table():
    view_data_pre_str = 'SELECT * FROM pre_table'
    c.execute(view_data_pre_str)
    data = c.fetchall()
    return data

#View data to vl_table
def view_data_to_vl_table():
    view_data_vl_str = 'SELECT * FROM vl_table'
    c.execute(view_data_vl_str)
    data = c.fetchall()
    return data

#View data to dl_table
def view_data_to_dl_table():
    view_data_dl_str = 'SELECT * FROM dl_table'
    c.execute(view_data_dl_str)
    data = c.fetchall()
    return data

#View data to pc_table
def view_data_to_pc_table():
    view_data_pc_str = 'SELECT * FROM pc_table'
    c.execute(view_data_pc_str)
    data = c.fetchall()
    return data

#View data to dc_table
def view_data_to_dc_table():
    view_data_dc_str = 'SELECT * FROM dc_table'
    c.execute(view_data_dc_str)
    data = c.fetchall()
    return data

#View data to be_table
def view_data_to_be_table():
    view_data_be_str = 'SELECT * FROM be_table'
    c.execute(view_data_be_str)
    data = c.fetchall()
    return data

#View data to po_table
def view_data_to_po_table():
    view_data_po_str = 'SELECT * FROM po_table'
    c.execute(view_data_po_str)
    data = c.fetchall()
    return data

#View data to op_table
def view_data_to_op_table():
    view_data_op_str = 'SELECT * FROM op_table'
    c.execute(view_data_op_str)
    data = c.fetchall()
    return data

#-------------------------------------------------------LIST_DEPOT FROM_MAIN_TABLE-----------------------------------------------------------------#
#list depot from main table
def list_all_depots():
    c.execute('SELECT DISTINCT depot FROM main_table')
    data = c.fetchall()
    return data

#MAY NEED TO LIST FROM OTHER TABLES (DEPENDS ON SELECT FUNCTION)

#-------------------------------------------------------GET_DEPOT FROM_MAIN_TABLE----------------------------------------------------------
#get depot from main table
def get_depot_by_depot_name_main(depot):
    c.execute('SELECT * FROM main_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from pre table
def get_depot_by_depot_name_pre(depot):
    c.execute('SELECT * FROM pre_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from vl table
def get_depot_by_depot_name_vl(depot):
    c.execute('SELECT * FROM vl_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from dl table
def get_depot_by_depot_name_dl(depot):
    c.execute('SELECT * FROM dl_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from pc table
def get_depot_by_depot_name_pc(depot):
    c.execute('SELECT * FROM pc_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from dc table
def get_depot_by_depot_name_dc(depot):
    c.execute('SELECT * FROM dc_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from be table
def get_depot_by_depot_name_be(depot):
    c.execute('SELECT * FROM be_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from po table
def get_depot_by_depot_name_po(depot):
    c.execute('SELECT * FROM po_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data

#get depot from op table
def get_depot_by_depot_name_op(depot):
    c.execute('SELECT * FROM op_table WHERE depot="{}"'.format(depot))
    data = c.fetchall()
    return data
    


#-------------------------------------------------------EDIT_DATA_FROM_TABLES-----------------------------------------------------------------#
#edit data to main_table
def edit_data_to_main_table():
    edit_data_main_str = ''
    c.execute(edit_data_main_str, ())

#edit data to pre_table
def edit_data_to_select_table_select_1a(select_1a):
    edit_data_select_str = f"""UPDATE select_table SET select_1a =?"""
    c.execute(edit_data_select_str, (select_1a,))
    conn.commit()
    data = c.fetchall()
    return data
#edit data to pre_table
def edit_data_to_select_table_select_1b(select_1b):
    edit_data_select_str = f"""UPDATE select_table SET select_1b =?"""
    c.execute(edit_data_select_str, (select_1b,))
    conn.commit()
    data = c.fetchall()
    return data

#edit data to pre_table
def edit_data_to_pre_table_pre_HM(pre_HM, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_HM =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_HM, depot))
    conn.commit()
    data = c.fetchall()
    return data
#CONTINUE THIS METHOD UPDATING A SINGLE VARIABLE AT A TIME 
def edit_data_to_pre_table_pre_dh(pre_dh, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_dh =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_dh, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_eo(pre_eo, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_eo =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_eo, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_info(pre_info, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_info =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_info, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_DT(pre_DT, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_DT =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_DT, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_metric(pre_metric, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_metric =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_metric, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_val(pre_val, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_val =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_val, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_HM_text(pre_HM_text, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_HM_text =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_HM_text, depot))
    conn.commit()
    data = c.fetchall()
    return data


def edit_data_to_pre_table_pre_HM_diff(pre_HM_diff, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_HM_diff =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_HM_diff, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_dh_text(pre_dh_text, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_dh_text =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_dh_text, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_dh_diff(pre_dh_diff, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_dh_diff =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_dh_diff, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_eo_diff(pre_eo_diff, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_eo_diff =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_eo_diff, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_pre_table_pre_eo_text(pre_eo_text, depot):
    edit_data_pre_str = f"""UPDATE pre_table SET pre_eo_text =? where depot =?"""
    c.execute(edit_data_pre_str, (pre_eo_text, depot))
    conn.commit()
    data = c.fetchall()
    return data







    query = """ UPDATE books
                SET title = %s
                WHERE id = %s "
                """
    



#edit data to pre_table
def edit_data_to_pre_table_DONE(pre_HM, pre_dh, pre_eo, pre_DT):
    edit_data_pre_str_done = 'UPDATE pre_table SET pre_HM ="DONE", pre_dh ="DONE", pre_eo="DONE", pre_DT=pre_DT WHERE pre_HM =? and pre_dh =? and pre_eo=? and pre_DT=?'
    c.execute(edit_data_pre_str_done, (pre_HM, pre_dh, pre_eo, pre_DT))
    
    data = c.fetchall()
    return data

#vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_papre_tr, vl_info ,vl_DT
#edit data to vl_table
def edit_data_to_vl_table_vl_algo(vl_algo, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_algo =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_algo, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_cost(vl_cost, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_cost =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_cost, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_dep_set(vl_dep_set, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_dep_set =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_dep_set, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_dead_cat(vl_dead_cat, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_dead_cat =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_dead_cat, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_mid_park(vl_mid_park, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_mid_park =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_mid_park, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_pre_tr(vl_pre_tr, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_pre_tr =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_pre_tr, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_info(vl_info, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_info =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_info, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_DT(vl_DT, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_DT =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_DT, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_vl_table_vl_metric(vl_metric, depot):
    edit_data_vl_str = f"""UPDATE vl_table SET vl_metric =? where depot =?"""
    c.execute(edit_data_vl_str, (vl_metric, depot))
    conn.commit()
    data = c.fetchall()
    return data


def edit_data_to_dl_table_dl_travel(dl_travel, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_travel =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_travel, depot))
    conn.commit()
    data = c.fetchall()
    return data
    

def edit_data_to_dl_table_dl_pref_gr(dl_pref_gr, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_pref_gr =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_pref_gr, depot))
    conn.commit()
    data = c.fetchall()
    return data



def edit_data_to_dl_table_dl_spl_br(dl_spl_br, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_spl_br =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_spl_br, depot))
    conn.commit()
    data = c.fetchall()
    return data

def edit_data_to_dl_table_dl_duty_breaks(dl_duty_breaks, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_duty_breaks =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_duty_breaks, depot))
    conn.commit()
    data = c.fetchall()
    return data
    
   

def edit_data_to_dl_table_dl_DT(dl_DT, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_DT =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_DT, depot))
    conn.commit()
    data = c.fetchall()
    return data
   
def edit_data_to_dl_table_dl_metric(dl_metric, depot):
    edit_data_dl_str = f"""UPDATE dl_table SET dl_metric =? where depot =?"""
    c.execute(edit_data_dl_str, (dl_metric, depot))
    conn.commit()
    data = c.fetchall()
    return data


#edit data to dl_table
def edit_data_to_dl_table():
    edit_data_dl_str = ''
    c.execute(edit_data_dl_str, ())

#edit data to pc_table
def edit_data_to_pc_table():
    edit_data_pc_str = ''
    c.execute(edit_data_pc_str, ())

#edit data to dc_table
def edit_data_to_dc_table():
    edit_data_dc_str = ''
    c.execute(edit_data_dc_str, ())

#edit data to be_table
def edit_data_to_be_table():
    edit_data_be_str = ''
    c.execute(edit_data_be_str, ())

#edit data to po_table
def edit_data_to_po_table():
    edit_data_po_str = ''
    c.execute(edit_data_po_str, ())

#edit data to op_table
def edit_data_to_op_table():
    edit_data_op_str = ''
    c.execute(edit_data_op_str, ())

#delete recird 

def delete_data_to_main_table(depot):
    delete_data_main_Table_str =  f"""DELETE FROM main_table WHERE depot =?"""
    c.execute(delete_data_main_Table_str, (depot,))
    data = c.fetchall()
    return data

def delete_data_to_pre_table(depot):
    delete_data_pre_Table_str =  f"""DELETE FROM pre_table WHERE depot =?"""
    c.execute(delete_data_pre_Table_str, (depot,))
    data = c.fetchall()
    return data

def delete_data_to_vl_table(depot):
    delete_data_vl_Table_str =  f"""DELETE FROM vl_table WHERE depot =?"""
    c.execute(delete_data_vl_Table_str, (depot,))
    data = c.fetchall()
    return data

def delete_data_to_dl_table(depot):
    delete_data_dl_Table_str =  f"""DELETE FROM dl_table WHERE depot =?"""
    c.execute(delete_data_dl_Table_str, (depot,))
    data = c.fetchall()
    return data