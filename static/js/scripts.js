  
// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  let captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}


let dataSetUser = [
  ['1', 'Tiger Nixon', 'System Architect'],
  ['2', 'Garrett Winters', 'Accountant'],
  ['3', 'Ashton Cox', 'Junior Technical Author'],
  ['4', 'Cedric Kelly', 'Senior Javascript Developer'],
]

let dataSetAsset = [
  ['1', 'Mask', '123-456', 100 , 'None'],
  ['2', 'Glove', '111-222', 100, 'None'],
  ['3', 'Medical Cap', '001-112', 100, 'None'],
  ['4', 'Sanitiser', '000-001', 100, 'None'],
]

//Asset List Table
$(document).ready(function () {
  $('#assetListTable').DataTable({

  });
});

//Requested List Table
$(document).ready(function () {
  $('#requestedListTable').DataTable({
      data: dataSetAsset,
      columns: [
          { title: '#' },
          { title: 'Product Name' },
          { title: 'Serial-Code' },
          {title: 'Quantity'},
          {title: 'Status'},
      ],
  });
});

//Request To Table for manager
$(document).ready(function () {
  $('#requestToTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent: '<select class="form-select" aria-label="Default select example">' +
          '<option selected></option>' +
          '<option value="1">Request to OTHER Hospital</option>' +
          '<option value="2">Reject</option>' +
          '</select>',
      },
  ],
      data: dataSetAsset,
      columns: [
          { title: '#' },
          { title: 'Product Name' },
          { title: 'Serial-Code' },
          {title: 'Quantity'},
          {title: 'Status'},
          {title: 'Action'},
      ],
  });
});

//Request FROM for manager
$(document).ready(function () {
  $('#requestFromTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent:
          '<a href="approve/">' +
          '<input type="button" class="btn btn-primary" value="Click" />'+
          '</a>',
      },
  ],
      data: dataSetAsset,
      columns: [
          { title: '#' },
          { title: 'Product Name' },
          { title: 'Serial-Code' },
          {title: 'Quantity'},
          {title: 'Status'},
          {title: 'Action'},
      ],
  });
});

//Admin table to add, edit, delete asset
$(document).ready(function () {
  $('#manageAssetTable').DataTable({});
});

//SELECT Asset List Table
$(document).ready(function () {
  $('#selectAssetTable').DataTable({});
});



$(document).ready(function () {
  $('#manageInvList').DataTable({});
});


$('.add-to-list').click(function () {
  var id;
  var url;
  id = $(this).attr("data-catid");
  url = $(this).attr("to_java");
  console.log(id);
  $.ajax(
      {
          type: "GET",
          url: url,
          data: {
              item_id: id
          },
          success: function (data) {
            $('#selectAssetTable').ajax.reload();
            // $('#add-to-list' + id).removeClass('btn btn-primary btn-block');
            // $('#add-to-list' + id).addClass('btn btn-success btn-block');
            // $('#add-to-list' + id).text('Added to the shopping list');
          }
      })
});