
import hydralit_components as hc

modal_code = """
    <div>
    <!-- Button trigger modal -->

    <style>
    .btnCenter{
        top:15%;
        transform:translateY(-38%)
       
    }
    </style>
 
    <button type="button" class="btn btn-info btnCenter" data-toggle="modal" data-target="#exampleModal">
    <i class="bi bi-plus">+</i>
    </button>

    <!-- Modal Center Code -->
    <style>
    .modalCenter{
        top:20%;
        transform:translateY(-30%)
    }
    </style>
    <!-- Modal -->
    

    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modalCenter" role="document">
    <div class="modal-content">
    <div class="modal-header">
    <h5 class="modal-title" id="exampleModalLabel">Add Additional Comment</h5>
    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
        <span aria-hidden="true">&times;</span>
    </button>
    </div>
    <div class="modal-body">
    <div class="container">
   
    <form class="form-horizontal" action="/" onsubmit="myFunction(event)"">
    <div class="form-group">
    <label class="control-label col-sm-2" >Algo Parameters</label>
    <div class="col-sm-10">
    <input type="text" class="form-control" id="vl_algo" name="vl_algo">
    </div>

    </div>
   
    <div class="form-group">        
    <div class="col-sm-offset-2 col-sm-10">
    <button type="submit" class="btn btn-default">Submit</button>
    </div>
    </div>
    </form>
    <script>
  function myFunction(event){
    event.preventDefault();
    //code here
  }
  </script>
    </div>
    </div>
    <div class="modal-footer">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
    </div>
    </div>
    </div>
    </div>
    </div>
    """




# create count index based on route row duplicates 
# if count row index is one for subsequent unique routes, check if 1 and stop is equal for any atco
# categorical data 


#archived code from before get data from depot table: just incase it is needed
'''#Get all data from pre_table
    all_depots_pre = db.view_data_to_pre_table()

    for i in all_depots_pre:
        depot = i[0]
        pre_HM = i[1]
        pre_dh = i[2]
        pre_eo = i[3]
        pre_info = i[4]
        pre_DT = i[5]
        pre_metric = i[6]
        pre_val = i[7]
        pre_HM_text = i[8]
        pre_dh_text = i[9]
        pre_HM_diff =i[10]
        pre_dh_diff = i[11]
        pre_eo_diff = i[12]
        pre_eo_text = i[13]'''

#Keep these labels just in case


label_style1a = """
<div style="background-color:#06582C;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
<p style="color:white;text-align:center;font-size:15px">{}</p>
</div>
"""
label_style1b = """
<div style="background-color:#62911A;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
<p style="color:white;text-align:center;font-size:15px">{}</p>
</div>
"""

label_style1c = """
<div style="background-color:#91811A;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
<p style="color:white;text-align:center;font-size:15px">{}</p>
</div>
"""

label_style1d = """
<div style="background-color:#91571A;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
<p style="color:white;text-align:center;font-size:15px">{}</p>
</div>
"""

label_style1e = """
<div style="background-color:#911A1A;padding:2px;border-radius:18px;margin:1px; height: 28px; width: 22%;">
<p style="color:white;text-align:center;font-size:15px">{}</p>
</div>
"""

#status labels

label_style1 = """
<div style="background-color:#464e5f;padding:5px;border-radius:5px;margin:9px; height: 38px; width: 50%;">
<p style="color:white;text-align:center;">{}</p>
</div>
"""


label_style2 = """
<div style="background-color:#196F27;padding:5px;border-radius:5px;margin:9px; height: 38px; width: 50%;">
<p style="color:white;text-align:center;">{}</p>
</div>
"""

label_style3 = """
<div style="background-color:#924010;padding:5px;border-radius:5px;margin:9px; height: 38px; width: 50%;">
<p style="color:white;text-align:center;">{}</p>
</div>
"""