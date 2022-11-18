from cProfile import label
from io import BytesIO
from sched import scheduler
import streamlit as st
import db
from datetime import datetime
from streamlit_card import card
import time 
import pandas as pd
import hydralit_components as hc

import dataclasses as dataclass

import pdb
from io import BytesIO

from functools import partial
from fpdf import FPDF
from create_table_fpdf2 import PDF



st.set_page_config(page_title="Tracker",layout='wide')

#NEED TO SEGREATE CUSTOM HTML INTO ITS OWN FILE AND IMPORT IT AT SOME POINT


#varibles for number difficultes
def gen_style1(colour):
    label_style1_pre = """
    <div style="background-color:#"""
    label_style1_post = """
    ;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
    <p style="color:white;text-align:center;font-size:15px">{}</p>
    </div>"""
    return label_style1_pre + colour + label_style1_post

#reference to key value pair within function
#style1_colour = {'a':'06582C','b':'62911A','c':'91811A','d':'91571A','e':'911A1A'}
#label_style1a = gen_style1(style1_colour['a'])

def gen_style2(colour):
    label_style2_pre = """
<div style="background-color:#"""
    label_style2_post = """;padding:5px;border-radius:5px;margin:9px; height: 38px; width: 50%;">
<p style="color:white;text-align:center;">{}</p>
</div>
"""
    return label_style2_pre + colour + label_style2_post







vert_space = '<div style="padding: 8px 5px;"></div>'
vert_spaceC = '<div style="padding: 1px 1px;"></div>'
vert_space_B = '<div style="padding: 9px 5px;"></div>'

vert_space_B1 = '<div style="padding: 1px 1px;"></div>'

vert_space3 = '<div style="padding: 10px 5px;"></div>'
vert_space3a = '<div style="padding: 11px 5px;"></div>'
vert_space4 = '<div style="padding: 13px 5px;"></div>'

vert_space5 = '<div style="padding: 24px 5px;"></div>'
vert_space5a = '<div style="padding: 20px 5px;"></div>'
vert_space6 = '<div style="padding: 26px 5px;"></div>'
vert_space7 = '<div style="padding: 28px 5px;"></div>'

vert_space2 = '''<div style="padding: 0px 0px;margin:0px">
<p style="color:black;text-align:center;">{}%</p>
</div>'''

#MAYBE CREATE A FILE FOR THESE VARIABLES ALSO



pre_HM, pre_dh, pre_eo, pre_info= 'ToDo', 'ToDo', 'ToDo', ''
vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info= 'ToDo', 'ToDo', 'ToDo','ToDo', 'ToDo','ToDo', ''
dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info= 'ToDo', 'ToDo', 'ToDo','ToDo', ''
pre_metric = 0
vl_metric = 0
dl_metric = 0
pre_val = ''
pre_HM_text = ''
pre_dh_text = ''
pre_HM_diff = 3
pre_dh_diff = 3
pre_eo_text = ''
pre_eo_diff = 3


# function for adding a depot from dedicated page
def add_depot():
    
    #if no SQL table created, it will create a tables 
    db.create_main_table()
    db.create_pre_table()
    db.create_vl_table()
    db.create_dl_table()
    #var x used to control button disabled state for add depot
    #TODO Change all this logic to a form 

    #control on button ui (colour)
    st.subheader('Add Depot')

    with st.form('Form', clear_on_submit=True):
        #create columns for presentation of inputs
        col80, col20 = st.columns([4,1])
      
            #text for depot name 
        depot = col80.text_input('Enter Depot Name'+'*')
            #description for depot 
        
        
        info = st.text_area('Enter Additional Info (optional)')
            
        #scheduler_name text input
        scheduler_name = st.text_input('Enter Scheduler Name')
        #se_name text input 
        se_name = st.text_input('Enter SE Name')
        #if depot value is not empty, disabled button = False - Form validation
            
        
        #create space to get button aligned with text field
        col20.markdown('')
        col20.markdown('')
        #Button to add depot to database and other associated data
        add_d = col20.form_submit_button('+') 
    #if add button is clicked (true)
        if add_d:
            #get datetime and assign to variable to track when record is created 
            if depot =='':
                e_dt = st.empty()
                e_dt.info('Depot cannot be **None**', icon='ℹ️')
                for sec in range(3,0,-1): 
                    time.sleep(1)
                if sec == 1:
                    e_dt.empty()
                
            else:
                depot_upper = depot.upper()
                all_depots_main = db.view_data_to_main_table()
                #List comprehension 
                    #list of first columns of main table and converted to upper
                new = [i[0].upper() for i in all_depots_main]
                
                if depot_upper in new:
                    e_dt = st.empty()
                    e_dt.warning(f'Depot: **{depot}** Already exists in database')
                    for sec in range(3,0,-1): 
                        time.sleep(1)
                    if sec == 1:
                        e_dt.empty()
            
                else: 
                    main_dt_r = datetime.now()
                    main_dt = main_dt_r.strftime("%H:%M on %d/%m/%Y")
                    #datetimes for all other sections of record - audit
                    pre_DT = main_dt_r.strftime("%H:%M on %d/%m/%Y")
                    vl_DT = main_dt_r.strftime("%H:%M on %d/%m/%Y")
                    dl_DT = main_dt_r.strftime("%H:%M on %d/%m/%Y")

                    #add data from form to maintable
                    db.add_data_to_main_table(depot, info, scheduler_name, se_name, main_dt)
                    #add default values to all other tables (this will be updated by edit functions in the view_progress function())
                    db.add_data_to_pre_table(depot, pre_HM, pre_dh, pre_eo, pre_info, pre_DT, pre_metric, pre_val, pre_HM_text, pre_dh_text, pre_HM_diff, pre_dh_diff, pre_eo_diff, pre_eo_text)
                    db.add_data_to_vl_table(depot, vl_algo, vl_cost, vl_dep_set, vl_dead_cat, vl_mid_park, vl_pre_tr, vl_info ,vl_DT, vl_metric)
                    db.add_data_to_dl_table(depot, dl_travel, dl_pref_gr, dl_spl_br, dl_duty_breaks, dl_info, dl_DT, dl_metric)
                    #Create a notification success message for record creation, this will be held in an empty container so it can be removed (temporary)
                    t_dt = st.empty()
                    #success message
                    t_dt.success(f'Depot: **{depot}** Saved at {main_dt}')
                    #Defining time for count before message dissapears
                    for sec in range(3,0,-1): 
                        time.sleep(1)
                    if sec == 1:
                        t_dt.empty()



#function for viewing and editing created records
def view_progress():
   

    #return list of depot names for selection via a select box
    all_depots_list_main = [i[0] for i in db.list_all_depots()]

    #render the select box 
    depot_select = st.sidebar.selectbox(label='', options = all_depots_list_main, label_visibility='hidden')
    #retrieve data based on the data selected
    

    
    depot_list_result_main = db.get_depot_by_depot_name_main(depot_select)
    for i in depot_list_result_main:
        depot = i[0]
        info = i[1]
        scheduler_name = i[2]
        se_name = i[3]
        main_dt = i[4]

    st.subheader(depot)

    cola, colb, colc, cold = st.columns([3,1,1,1])
    
    sch_name = 'Scheduler Name:'
    colb.caption(f'{sch_name} {scheduler_name}')
    
    se_name_str = 'Solution Engineer Name:'
    colc.caption(f'{se_name_str} {se_name}')
    
    cold.caption(f'Record Created: {main_dt}')

    cola.markdown(f'**General Information:** {info}')



    depot_list_result_pre = db.get_depot_by_depot_name_pre(depot_select)

    
    for i in depot_list_result_pre:
        depot = i[0]
        pre_HM = i[1]
        pre_dh = i[2]
        pre_eo = i[3]
        pre_info = i[4]
        pre_DT = i[5]
        pre_metric= i[6]
        pre_val = i[7]
        pre_HM_text = i[8]
        pre_dh_text = i[9]
        pre_HM_diff = i[10]
        pre_dh_diff = i[11]
        pre_eo_diff = i[12]
        pre_eo_text = i[13]




    ################# PRE _ REQUISITES FUNCTIONALITY


    st.markdown('---')

    #this variable is used to control a bug with the expander, when it auto collapses due to a variable change in the title
    expand_pre = False
    #Logic for UI
    if pre_metric == 100:
        icon_pre = '✅'
        expand_pre = True
    else:
        icon_pre = ''
        expand_pre = True


    #Create expander to hold content for pre_requisites
    pre_expander  = st.expander(f'Pre-requisites: {pre_metric}% {icon_pre}', expanded=expand_pre)

    #Create function that allows the checkbox state to be reset upon button click for save or all
    def reset_button():
        #pre val is the default value that controls the session state for key 'p'
        if pre_val=='False':   
            st.session_state["p"] = False
            
        elif pre_val == 'True':
            st.session_state["p"] = True


    
    #Content inside exapnder
    with pre_expander: 
        #Content spacer
        st.markdown('')
        #6 columns for the expander
        col1, col1aa, col1a, col2, col3, col4, col5 = st.columns([9,18,5,5,5,5,2])
        #List used to check all variable statuses in expander
        pre_list = [pre_HM, pre_dh, pre_eo]
        #List to declare all statuses of the expander
        pre_done_values = ['Done', 'Done', 'Done']
        #condition that controls the state of the button based on balues being all done, if all done, all button is disabled
        if pre_list ==pre_done_values:
            btn_all_state = True
        else:
            btn_all_state= False

        #Creating a mark all done button 
        all_pre = col1.button('Mark All Done', on_click=reset_button, disabled=btn_all_state)
        #If clicked
        if all_pre:
            #Assign completion metric to 100 percent
            pre_metric = 100
            # Assign all variables relevant to done status - FIND A MORE EFFICIENT SOLUTION?
            pre_HM, pre_dh, pre_eo = 'Done', 'Done', 'Done'
            #Get datetime of update
            pre_dt_r = datetime.now()
            #Format date time to relevant structure 
            pre_DT = pre_dt_r.strftime("%H:%M on %d/%m/%Y")
            #Update database records for relevant variables
            db.edit_data_to_pre_table_pre_HM(pre_HM, depot)
            db.edit_data_to_pre_table_pre_dh(pre_dh, depot)
            db.edit_data_to_pre_table_pre_eo(pre_eo, depot)
            db.edit_data_to_pre_table_pre_DT(pre_DT, depot)
            db.edit_data_to_pre_table_pre_metric(pre_metric, depot)
            


        #checkbox you want the button to un-check
        #uses the session state variable of p as a control from the save and mark all button
        edit_pre = col2.checkbox("Edit", key='p')
        # if edit checkbox is clicked/checked
        if edit_pre == True: 
            # the save button state is enabled (disabled set to false), and button colour change based on type: primary
            btn_type, btn_state = 'primary', False
            
        else:
            # button disabled if not in edit mode, secondary type assisgned to save button
            btn_type, btn_state = 'secondary', True
            
            #info icon with hyperlink to scheduling manual - WANT TO CREATE THIS CONTENT IN A LINKED PAGE INSTEAD OF EXTERNAL LINK TO DOCUMENT
            #link_pre = f'[<i class="material-icons" style="font-size: 1.5em; padding-right: 3x; padding-top:5px;">information</i>](https://docs.google.com/document/d/1qVBB6hDFtGlPU6rykVXNgbtC8IjzTJqbk3M2IaT9Mdc/edit#bookmark=id.ou7ok9njwhr9)'
            #display icon
            #THIS IS COMMENTED OUT FOR NOW AS AMENDS PADDING LOGIC TO COMMENTS
            #col1aa.caption(link_pre, unsafe_allow_html=True)
    
        #declare save button variable now conditions for its state have been defined 
        
    
        save_pre=col4.button('Save', on_click=reset_button, type=btn_type, disabled=btn_state)
        
        
        #line spacer at bottom of container
        st.markdown('---')
        #store statuses and pre_req info in container for control of content
        pre_contents = st.container()

        
        
        with pre_contents:
            #Write content for each section 
                # WOULD BE NICE TO EITHER STORE THESE IN DB OR IMPORT FROM ANOTHER CONTENT FILE _ SAVE LINESPACE
            col1.write('**Hours and Miles**')
            #Insert vertical space below to ensure correct content row alignment in columns 
            col1.markdown(vert_space, unsafe_allow_html=True)
            #/-same as above
            col1.write('**Missing Deadheads**')
            #/-same as above
            col1.markdown(vert_space, unsafe_allow_html=True)
            #/-same as above
            col1.write('**Overlapping Deadheads**')
            #/-same as above

            #edit checkbox is ticked - Multiple declarations 
            if edit_pre==True:
                #Spacer on column for content alignment - CONSILIDATE INTO FUNCTION OR ONE LINE TO SAVE LINESPACE
                col1a.markdown('')
                #/-same as above
                col1aa.markdown('')
                #/-same as above
                col3.markdown('')
                
                
                #Write text input for first variable of section - label should be presented
                pre_HM_text = col1aa.text_input(label='Comment',value= pre_HM_text, placeholder= 'make comment here', key ='pre_HM_text' )
                #reorder list options so when item is changed and reselected, it will present the value that has been saved first in the list
                list_options = ['Done', 'ToDo', 'Stuck']
                list_options.remove(pre_HM)
                list_options.insert(0, pre_HM)
            
                #number input for difficulty rating for variable
                pre_HM_diff = col3.number_input(label = 'Difficulty', min_value=1, max_value=5, value =pre_HM_diff,step=1, key= 'pre_HM_diff')
                #/-same as above
                pre_dh_diff = col3.number_input(label = 'Difficulty', min_value=1, max_value=5, value =pre_dh_diff,step=1, key= 'pre_dh_diff', label_visibility='collapsed')
                #/-same as above
                pre_eo_diff = col3.number_input(label = 'Difficulty', min_value=1, max_value=5, value =pre_eo_diff,step=1, key= 'pre_eo_diff', label_visibility='collapsed')

                #status selectbox based on list options (see logic fro line 435)
                pre_HM = col1a.selectbox(label='Status', options = list_options, key= 'pre_HM')
                #same logic as line 432
                pre_dh_text = col1aa.text_input(label='Comment',value= pre_dh_text, placeholder= 'make comment here', key ='pre_dh_text', label_visibility='collapsed')
                #same logic as line 435
                list_options2 = ['Done', 'ToDo', 'Stuck']
                list_options2.remove(pre_dh)
                list_options2.insert(0, pre_dh)

                
                #same logic as line 446
                pre_dh = col1a.selectbox(label='pre_dh', options = list_options2, label_visibility='collapsed')
                #same logic as line 432
                pre_eo_text = col1aa.text_input(label='Comment',value= pre_eo_text, placeholder= 'make comment here', key ='pre_eo_text', label_visibility='collapsed')
                #same logic as line 435
                list_options3 = ['Done', 'ToDo', 'Stuck']
                list_options3.remove(pre_eo)
                list_options3.insert(0, pre_eo)

                #same logic as line 446
                pre_eo = col1a.selectbox(label='pre_eo', options =list_options3, label_visibility='collapsed')
                #Present text area for further section info
                pre_info = st.text_area('Pre-requisites Info', value=pre_info)
                #Variable to update state on checkbox - when set to True - check is still true
                pre_val='True'
                #edit value in database to ensure persistent edit_pre state
                db.edit_data_to_pre_table_pre_val(pre_val, depot)
                #if mark all done button is clicked (TRUE)
                if all_pre:
                    #State variable changes, thus changing check value to False and closing edit checkbox
                    pre_val = 'False'
                    #db variable updated so state is persistent
                    db.edit_data_to_pre_table_pre_val(pre_val, depot)

                #if save button is clicked (TRUE)
            
                if save_pre:
                    
                    #State variable to change edit state, same logic as line 475
                    pre_val='False'
                    #upon save, get datatime data for event 
                    pre_dt_r = datetime.now()
                    #format datetime - CREATE FUNCTION to use this across app rather than repeating method
                    pre_DT = pre_dt_r.strftime("%H:%M on %d/%m/%Y")

                    #Update all database records upon save - persistent state next time app page is rendered 
                    db.edit_data_to_pre_table_pre_HM(pre_HM, depot)
                    db.edit_data_to_pre_table_pre_dh(pre_dh, depot)
                    db.edit_data_to_pre_table_pre_eo(pre_eo, depot)
                    db.edit_data_to_pre_table_pre_info(pre_info, depot)
                    db.edit_data_to_pre_table_pre_DT(pre_DT, depot)
                    db.edit_data_to_pre_table_pre_val(pre_val, depot)
                    db.edit_data_to_pre_table_pre_HM_text(pre_HM_text, depot)
                    db.edit_data_to_pre_table_pre_dh_text(pre_dh_text, depot)
                    db.edit_data_to_pre_table_pre_HM_diff(pre_HM_diff, depot)
                    db.edit_data_to_pre_table_pre_dh_diff(pre_dh_diff, depot)
                    db.edit_data_to_pre_table_pre_eo_diff(pre_eo_diff, depot)
                    db.edit_data_to_pre_table_pre_eo_text(pre_eo_text, depot)
                    
                
                    close_pre = col5.button('x', on_click=reset_button, type= 'primary')
                    



            #while the edit button is false - display static content            
            if edit_pre == False:
                #import custom icons from material icons library
                st.markdown('<style>' + open('tracker.css').read() + '</style>', unsafe_allow_html=True)

                #spacing for text alignment
                col1aa.markdown(vert_space6, unsafe_allow_html=True)
                #when string is not empty for comment value
                if pre_HM_text != '':
                    #present icon (as comment made)
                    col1aa.caption(f'<i class="material-icons" style="font-size: 1.0em; padding-right: 10px;">comment</i>' + pre_HM_text , unsafe_allow_html=True)
                #if empty string 
                else:
                    #present spacer for column icon and also empty variable string 
                    col1aa.markdown(vert_space3a, unsafe_allow_html=True)
                    col1aa.caption(pre_HM_text)
                #spacing for text alignment
                col1aa.markdown(vert_space3, unsafe_allow_html=True)
                #same logic as above
                if pre_dh_text != '':
                    col1aa.caption(f'<i class="material-icons" style="font-size: 1.0em; padding-right: 10px;">comment</i>' + pre_dh_text , unsafe_allow_html=True)
                    
                else:
                    col1aa.markdown(vert_space3a, unsafe_allow_html=True)
                    col1aa.caption(pre_dh_text)
                col1aa.markdown(vert_space3, unsafe_allow_html=True)
                #same logic as above
                if pre_eo_text != '':
                    col1aa.caption(f'<i class="material-icons" style="font-size: 1.0em; padding-right: 10px;">comment</i>' + pre_eo_text , unsafe_allow_html=True)
                else:
                    col1aa.caption(pre_eo_text)
            
            #present static content regardless of state of checkbox 
            #list for styles - EVENTUALLY LOOK AT MOVING THIS TO A CONTENT MANAGER FILE
            stylesla = ['464e5f', '196F27', '924010']

            stylesl = [gen_style2(i) for i in stylesla]
            #list of statuses - EVENTUALLY LOOK AT MOVING THIS TO A CONTENT MANAGER FILE
            list_status = ['ToDo', 'Done', 'Stuck']

            #based on list status, render style for status variable appropriatley - HEX background colour based on variable string selected
            col2.markdown(stylesl[list_status.index(pre_HM)].format(pre_HM),unsafe_allow_html=True )
            #same logic as above
            col2.markdown(stylesl[list_status.index(pre_dh)].format(pre_dh),unsafe_allow_html=True )
            #same logic as above
            col2.markdown(stylesl[list_status.index(pre_eo)].format(pre_eo),unsafe_allow_html=True )

            #list for styles for dificulty rating - EVENTUALLY LOOK AT MOVING THIS TO A CONTENT MANAGER FILE
            style_colour = ['06582C','62911A','91811A','91571A','911A1A']
            #styles = [label_style1a,label_style1b,label_style1c,label_style1d, label_style1e]
            styles = [gen_style1(i) for i in style_colour]
            #based on dificulty integer - select relevant style - Same logic as above 
            col4.markdown(styles[pre_HM_diff-1].format(pre_HM_diff),unsafe_allow_html=True)
            #content spacer 
            col4.markdown(vert_space4, unsafe_allow_html=True)
            #same logic as above
            col4.markdown(styles[pre_dh_diff-1].format(pre_dh_diff),unsafe_allow_html=True)
            #content spacer 
            col4.markdown(vert_space4, unsafe_allow_html=True)
            #same logic as above
            col4.markdown(styles[pre_eo_diff-1].format(pre_eo_diff),unsafe_allow_html=True)

            #Columns below for meta content on section
            colv, coln, colf = st.columns([2,4,1])

            #present record updated selection
            colv.caption(f"**Last Updated:**     *{pre_DT}*")
            #present info if it is not empty string
            if not pre_info == '':
                coln.caption(f"**Pre-requisite Notes:** *{pre_info}*")

            #Create a list of variables to track progress, we can get the length of the list to determine incremental progress 
            list_pre = [pre_HM, pre_dh, pre_eo]

            #Function to take pre_variable and the list itself. check if the variable is done, divide 100 by list len and round by 1
            #Otherwise return 0
            def assign_completness(pref_type, list):
                if pref_type == 'Done':
                    pref_value = round(100/len(list),1)
                else:
                    pref_value = 0
                return pref_value
            
            #Assign variables to the return statement 
            var_pre_hm = assign_completness(pre_HM, list_pre)
            var_pre_dh = assign_completness(pre_dh, list_pre)
            var_pre_eo = assign_completness(pre_eo, list_pre)

        #Create a list of these returned values 
        list_pre_val = [var_pre_hm, var_pre_dh, var_pre_eo]
        #Get a total value for the sum of these values, and if the value is greater than 99, round to 100 
        def round_pre(list):
            if sum(list) > 99:
                b_total = 100
                return b_total
            else:
                a_total = sum(list)
                return a_total

        #need to use the difficulty rating to account for premetric total
        pre_metric = round_pre(list_pre_val)

        db.edit_data_to_pre_table_pre_metric(pre_metric, depot)
        

        colf.caption(f'**{pre_metric}**% Complete {icon_pre}')
        
    
######################### END OF PRE SECTION #######################################

########################## Start of VL SECTION #####################################

    depot_list_result_vl = db.get_depot_by_depot_name_vl(depot_select)

    for i in depot_list_result_vl:
        depot = i[0]
        vl_algo = i[1]
        vl_cost= i[2]
        vl_dep_set= i[3]
        vl_dead_cat= i[4]
        vl_mid_park= i[5]
        vl_pre_tr= i[6]
        vl_info= i[7]
        vl_DT= i[8]
        vl_metric = i[9]

######################### END OF VL SECTION #######################################


############################ START OF DL SECTION####################################

    

    depot_list_result_dl = db.get_depot_by_depot_name_dl(depot_select)

    for i in depot_list_result_dl:
        depot = i[0]
        dl_travel = i[1]
        dl_pref_gr= i[2]
        dl_spl_br= i[3]
        dl_duty_breaks= i[4]
        dl_info= i[5]
        dl_DT= i[6]
        dl_metric= i[7]

######################### END OF DL SECTION #######################################


########################## MAIN STATS  ###############
    main_val = 50
    st.caption(f'Overall Progress: {main_val}%')
    main_progress = st.progress(main_val)

    st.empty()
    
    with st.empty():
        st.markdown('')

    st.sidebar.markdown('---')

    buffer= BytesIO()

    ########FPDF LIBRARY LOGIC FOR REPORTS - CONSIDER REPORTER SETTINGS BE PART OF A CONFIGURATION PAGE - WHICH FEEDS INTO THESE METHODS

    class PDF(FPDF):
        def header(pdf):
            pdf.image('alogo-2.png', 10,7, 25)
            pdf.set_font('helvetica', size= 11)
            pdf.set_text_color(25,25,112)
            pdf.set_xy(40, 10)
            pdf.multi_cell(90,7,f'{depot}\nSE Name: {se_name}', border = False, ln=0, align='L')
            pdf.set_xy(110, 10)
            pdf.multi_cell(90,7,f'{main_dt}\nScheduler Name: {sch_name}', border = False, ln=0, align='R')
        

            #NOT ABLE TO WRITE MORE ATTRIBUTESS INTO HEADER 
            #self.cell(100,10,f'Scheduler Name:{scheduler_name}', border = False, ln=0, align='C')
            ##self.cell(120,10,f'SE Name:{se_name}', border = False, ln=0, align='C')
            pdf.set_draw_color(25,25,112)
            pdf.set_line_width(.4)
            pdf.line(10, 30, 210, 30)

        #This needs to go into a class
        def create_table(self, table_data, title='', data_size = 10, title_size=12, align_data='L', align_header='L', cell_width='even', x_start='x_default',emphasize_data=[], emphasize_style=None,emphasize_color=(0,0,0)): 
            """
            table_data: 
                        list of lists with first element being list of headers
            title: 
                        (Optional) title of table (optional)
            data_size: 
                        the font size of table data
            title_size: 
                        the font size fo the title of the table
            align_data: 
                        align table data
                        L = left align
                        C = center align
                        R = right align
            align_header: 
                        align table data
                        L = left align
                        C = center align
                        R = right align
            cell_width: 
                        even: evenly distribute cell/column width
                        uneven: base cell size on lenght of cell/column items
                        int: int value for width of each cell/column
                        list of ints: list equal to number of columns with the widht of each cell / column
            x_start: 
                        where the left edge of table should start
            emphasize_data:  
                        which data elements are to be emphasized - pass as list 
                        emphasize_style: the font style you want emphaized data to take
                        emphasize_color: emphasize color (if other than black) 
            
            """
            default_style = self.font_style
            if emphasize_style == None:
                emphasize_style = default_style
            # default_font = self.font_family
            # default_size = self.font_size_pt
            # default_style = self.font_style
            # default_color = self.color # This does not work

            # Get Width of Columns
            def get_col_widths():
                col_width = cell_width
                if col_width == 'even':
                    col_width = self.epw / len(data[0]) - 1  # distribute content evenly   # epw = effective page width (width of page not including margins)
                elif col_width == 'uneven':
                    col_widths = []

                    # searching through columns for largest sized cell (not rows but cols)
                    for col in range(len(table_data[0])): # for every row
                        longest = 0 
                        for row in range(len(table_data)):
                            cell_value = str(table_data[row][col])
                            value_length = self.get_string_width(cell_value)
                            if value_length > longest:
                                longest = value_length
                        col_widths.append(longest + 4) # add 4 for padding
                    col_width = col_widths



                            ### compare columns 

                elif isinstance(cell_width, list):
                    col_width = cell_width  # TODO: convert all items in list to int        
                else:
                    # TODO: Add try catch
                    col_width = int(col_width)
                return col_width

            # Convert dict to lol
            # Why? because i built it with lol first and added dict func after
            # Is there performance differences?
            if isinstance(table_data, dict):
                header = [key for key in table_data]
                data = []
                for key in table_data:
                    value = table_data[key]
                    data.append(value)
                # need to zip so data is in correct format (first, second, third --> not first, first, first)
                data = [list(a) for a in zip(*data)]

            else:
                header = table_data[0]
                data = table_data[1:]

            line_height = self.font_size * 2.5

            col_width = get_col_widths()
            self.set_font(size=title_size)

            # Get starting position of x
            # Determin width of table to get x starting point for centred table
            if x_start == 'C':
                table_width = 0
                if isinstance(col_width, list):
                    for width in col_width:
                        table_width += width
                else: # need to multiply cell width by number of cells to get table width 
                    table_width = col_width * len(table_data[0])
                # Get x start by subtracting table width from pdf width and divide by 2 (margins)
                margin_width = self.w - table_width
                # TODO: Check if table_width is larger than pdf width

                center_table = margin_width / 2 # only want width of left margin not both
                x_start = center_table
                self.set_x(x_start)
            elif isinstance(x_start, int):
                self.set_x(x_start)
            elif x_start == 'x_default':
                x_start = self.set_x(self.l_margin)


            # TABLE CREATION #

            # add title
            if title != '':
                self.set_font('helvetica', size= 10, style='B')
                self.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=self.font_size)
                self.ln(line_height) # move cursor back to the left margin

            self.set_font(size=data_size)
            # add header
            y1 = self.get_y()
            if x_start:
                x_left = x_start
            else:
                x_left = self.get_x()
            x_right = self.epw + x_left
            if  not isinstance(col_width, list):
                if x_start:
                    self.set_x(x_start)
                for datum in header:
                    self.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
                    x_right = self.get_x()
                self.ln(line_height) # move cursor back to the left margin
                y2 = self.get_y()
                self.line(x_left,y1,x_right,y1)
                self.line(x_left,y2,x_right,y2)

                for row in data:
                    if x_start: # not sure if I need this
                        self.set_x(x_start)
                    for datum in row:
                        if datum in emphasize_data:
                            self.set_text_color(*emphasize_color)
                            self.set_font(style=emphasize_style)
                            self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size)
                            self.set_text_color(0,0,0)
                            self.set_font(style=default_style)
                        else:
                            self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                    self.ln(line_height) # move cursor back to the left margin
            
            else:
                if x_start:
                    self.set_x(x_start)
                for i in range(len(header)):
                    datum = header[i]
                    self.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
                    x_right = self.get_x()
                self.ln(line_height) # move cursor back to the left margin
                y2 = self.get_y()
                self.line(x_left,y1,x_right,y1)
                self.line(x_left,y2,x_right,y2)


                for i in range(len(data)):
                    if x_start:
                        self.set_x(x_start)
                    row = data[i]
                    for i in range(len(row)):
                        datum = row[i]
                        if not isinstance(datum, str):
                            datum = str(datum)
                        adjusted_col_width = col_width[i]
                        if datum in emphasize_data:
                            self.set_text_color(*emphasize_color)
                            self.set_font(style=emphasize_style)
                            self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size)
                            self.set_text_color(0,0,0)
                            self.set_font(style=default_style)
                        else:
                            self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                    self.ln(line_height) # move cursor back to the left margin
            y3 = self.get_y()
            self.line(x_left,y3,x_right,y3)

    #data for pre-requsites in df
    pre_titles = ["Name", 'Comment', "Status", 'Difficulty']
    pre_HM_row = ["Hours and Miles", pre_HM_text, pre_HM, str(pre_HM_diff)]
    pre_dh_row = ['Missing Deadheads' ,pre_dh_text, pre_dh, str(pre_dh_diff)]
    pre_eo_row = ['Overlapping Events', pre_eo_text, pre_eo, str(pre_eo_diff)]
    pre_information = [
    pre_titles, 
    pre_HM_row, 
    pre_dh_row,
    pre_eo_row
    ]

    #Consider making this function slightly more generic 

    #Thks is a function to take a preference, the status index from status list, and row data to create styling for the report
    def table_status_styling(pre_var, list_stat, row_data):
        if pre_var == list_stat:
            return_val_pre = row_data
        else:
            return_val_pre = []
        return return_val_pre

    pre_em_HM = table_status_styling(pre_HM, list_status[2], pre_HM_row)
    pre_em_dh = table_status_styling(pre_dh, list_status[2], pre_dh_row)
    pre_em_eo = table_status_styling(pre_eo, list_status[2], pre_eo_row)

    pre_em_pre = pre_em_HM + pre_em_dh + pre_em_eo




    
    pdf = PDF('P', 'mm', 'Letter')
    pdf.add_page()
    
    pdf.cell(10,10)

    pdf.ln()
    pdf.set_font('helvetica', size=10, style='B')
    pdf.multi_cell(200,5, f'Depot Information', border = False, ln=0, align='L')
    pdf.set_xy(10, 40)
    pdf.set_font('helvetica', size=10)
    #test this next cell
    pdf.set_xy(10, 45)

    pdf.multi_cell(200,5, info, border = False, ln=0, align='L')

    if len(info) < 45:
        pdf.set_xy(10, 55)
    pdf.create_table(table_data = pre_information, title = f'Pre Requisites: {pre_metric}%', title_size=10, data_size = 9, cell_width=[50,105,20,20], align_data='L', emphasize_data = pre_em_pre, emphasize_style='B', emphasize_color=(153, 55, 31))
    pdf.ln()


    
    
    pdf.set_auto_page_break(auto=True, margin=15)
    byte_string = pdf.output(dest="S")  # Probably what you want
    stream = BytesIO(byte_string)  # If you really need a BytesIO
    
    
    def dt_audit():
        pdf_dt_r = datetime.now()
        pdf_DT = pdf_dt_r.strftime("%H:%M on %d/%m/%Y")
        return pdf_DT

    pdf_filname = f'{depot} - {dt_audit()}'
    pdf = st.sidebar.download_button('Export PDF',  on_click =dt_audit, data=stream, file_name=f'{pdf_filname}.pdf')
        
            

    
    st.sidebar.button('Export XLSX')

        
    #if updated, pre_metric = old_pre_metric, pre_metric = new_pre_metric
    


    #define edit database methods for pre and vl. 
    #change the way edit works so it doesn't change the variables
    #create a pdf report with all information. 
    #implement overall progress bar for all sections. 
    # additional fields per preference
                


def home():
    colh, colj = st.columns([2,5])
    colh.subheader('Home')

    st.caption('See All Depot Record Summaries')
    all_depots_main = db.view_data_to_main_table()
    #Iterate through columns to get column values

    for i in all_depots_main:
        depot = i[0]
        info = i[1]
        scheduler_name = i[2]
        se_name = i[3]
        main_dt = i[4]

        h_et = st.empty()
        
        with h_et.expander(f'{depot}', expanded=True):
            
            st.caption(f'**Depot Information:** {info}')
            cola, colb, colc, cold = st.columns([3,3,3,1])
            cola.caption(f'**Scheduler Name:** {scheduler_name}')
            colb.caption(f'**SE_name:** {se_name}')
            colc.caption(f'**Created at:** *{main_dt}*')


                
                




    





    


   
    
def admin():
    st.subheader('Admin')

    p_em = st.empty()
    password_protect = p_em.text_input('Admin Password', type = 'password')

    if password_protect == '':
        st.info('To access this section please enter the correct password')

    elif password_protect != 'abc123':
        st.warning('Password Incorrect, please try again')
    

    elif password_protect == 'abc123':
        p_em.empty()

        all_depots_main = db.view_data_to_main_table()
        #Iterate through columns to get column values
        cols, colu, colk = st.columns([5,5,2])
        admin_del = colk.checkbox(label='Enable Delete')
        del_buta = True
        vad = 'secondary'
        if admin_del:
            del_buta = False
            vad = 'primary'

        del_str = ''
        for i in all_depots_main:
            depot = i[0]
            info = i[1]
            scheduler_name = i[2]
            se_name = i[3]
            main_dt = i[4]
            
            with st.form(depot):
        
                st.write(f'{depot}')

                st.write(f'*{main_dt}*')
                
                delx = st.form_submit_button('Delete', disabled= del_buta, type = vad)
                if delx:
                    db.delete_data_to_main_table(depot)
                    db.delete_data_to_pre_table(depot)
                    db.delete_data_to_dl_table(depot)
                    db.delete_data_to_vl_table(depot)
                    del_dt_r = datetime.now()
                    #format datetime - CREATE FUNCTION to use this across app rather than repeating method
                    del_DT = del_dt_r.strftime("%H:%M on %d/%m/%Y")
                    #TODO present info message about which depot has been deleted
                    #st.experimental_rerun()
                    d_et = st.empty()
                     #success message
                    d_et.success(f'Deleting Record: **{depot}** at {del_DT}')

                    with st.spinner('Please Wait'):
                        #Defining time for count before message dissapears
                        for sec in range(3,0,-1): 
                        
                                time.sleep(.8)
        
                        if sec == 1:
                            d_et.empty()
                            st.experimental_rerun()
                    


                        
                

        st.markdown('---')
        st.markdown('Generate Report templates')
        with st.form('Reports Config'):
            st.write('Report Config')
            #Logic for config goes here and is saved to the database so we can pull it back in the view depots section
            #consider on a per- user basis or per depot - EXPLORATION
            # OR Multiple templates stored as a selection by the user: 
                #TODO create templates that can be saved with various attributes to the database 
                #TODO Define template attributes: Name, Description, select meta information to include, Selectable date range, include all statuses or specific ones. 
            st.caption('Placeholder for logic ***')
            st.form_submit_button('Submit')

    


def main():




    choice=['Home', 'Add Depot', 'View Depots', 'Admin']
 
    choices= st.sidebar.selectbox(label='  ', options= choice)

    if choices == 'Home':
        
        home()

        #Create a table to return this logic and have a none value, and if button clicked, we return the depot value and the associated true/ false value, and when in the view progress method, we reset this value 

    if choices == 'Add Depot':
        add_depot()
    if choices =='View Depots':
        view_progress()
       
    if choices == 'Admin':
        admin()

    
        
    

if __name__ == '__main__':
    main()




# 1. Extend to Optimisations (a lot of info)
    # What GCs have we done and all exceptions
# 2. IMPORTANT - Approval process
    # Report configs:
        # 1 Export for clients - weekly external
        # 2 Export for internal purposes - Harry to check how he'd like to see the reports as (approved, comments, dates?)

####

# Add the following:
    # Data Migration
    # Benchmark Comparison
    # Optimizations result table
        # Link to schedule for internal purposes (already in the form above)
    #### ANY DELIVERABLES ####

# Store document in the Drive and link them to the app instead of uploading
    # Ensure max. characters in PostgresSQL