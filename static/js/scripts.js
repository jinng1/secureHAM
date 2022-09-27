  
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

//User Table
$(document).ready(function () {
  $('#userManagementTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent: '<select class="form-select" aria-label="Default select example">' +
          '<option selected></option>' +
          '<option value="1">Edit</option>' +
          '<option value="2">Delete</option>' +
          '</select>',
      },
  ],
      data: dataSetUser,
      columns: [
          { title: '#' },
          { title: 'Name' },
          { title: 'Position' },
          {title: 'Action'},
      ],
  });
});

//Asset List Table
$(document).ready(function () {
  $('#assetListTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent: '<a href="#" onclick="f1()" class="link-info">Request</a>',
      },
  ],
      data: dataSetAsset,
      columns: [
          { title: '#' },
          { title: 'Product Name' },
          { title: 'Serial-Code' },
          {title: 'Quantity'},
          {title: 'Status' , ID : "status"},
          {title: 'Action'},
      ],
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

//Manager table to add, edit, delete asset
$(document).ready(function () {
  $('#manageAssetTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent: '<select class="form-select" aria-label="Default select example">' +
          '<option selected></option>' +
          '<option value="1">Edit</option>' +
          '<option value="2">Delete</option>' +
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

//SELECT Asset List Table
$(document).ready(function () {
  $('#selectAssetTable').DataTable({
    columnDefs: [
      {
          targets: -1,
          data: null,
          className: "text-center",
          defaultContent: '<a href="#" onclick="f1()" class="link-info">Select</a>',
      },
  ],
      data: dataSetAsset,
      columns: [
          { title: '#' },
          { title: 'Product Name' },
          { title: 'Serial-Code' },
          {title: 'Quantity'},
          {title: 'Status' , ID : "status"},
          {title: 'Action'},
      ],
  });
});

function f1()
{
  
}