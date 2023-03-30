


const downloadButton = document.getElementById('download-button');
const selectYear = document.getElementById('select-year');
const selectedModel = document.querySelector( 'input[name="model"]:checked');   

downloadButton.addEventListener('click', () => {

  //Cedar collection
  var downloadUrl;
  var baseUrl = 'https://storage.googleapis.com/co2_app/GPP_CTE_ST_NT_BASE/GPP_CTE_ST_NT_BASE.zip?authuser=0'
  var hybridUrl = 'https://storage.googleapis.com/co2_app/GPP_CTE_ST_NT_HYBRID/GPP_CTE_ST_NT_HYBRID.zip?authuser=0'
  var mlUrl = 'https://storage.googleapis.com/co2_app/GPP_CTE_ST_NT_ML/GPP_CTE_ST_NT_ML.zip?authuser=0'
  
  var selectedModel = $('input[name="model"]:checked').val();
  downloadUrl = baseUrl;
  if(selectedModel =='GPP_CTE_ST_NT_ML'){
    downloadUrl = mlUrl;
  } else if(selectedModel =='GPP_CTE_ST_NT_HYBRID'){
    downloadUrl = hybridUrl;
  } 


  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute('href', downloadUrl);
  //downloadAnchor.setAttribute('target', '_blank');
  downloadAnchor.setAttribute('download', ''); // empty string sets the filename to the original filename
  downloadAnchor.click();
});

function enableDownload(){
  var selectedModel = $('input[name="model"]:checked').val();
  var selectedYear = $("#select-year").val();
  var selectedUse = $("#select-use").val();
  var textUsage = $("#textarea-use").val();
  var checkAck = $("#ack").prop('checked');
  return selectedYear != "" && selectedModel != "" && selectedUse != "" && textUsage != "" &&  checkAck
}

// Check the radio button value.
function modelselect() {

  if (enableDownload()) {
    $("#download-button").prop("disabled", false);
  } else {
    $("#download-button").prop("disabled", true);
  }
}

function selectuse() {
  if (enableDownload()) {
    $("#download-button").prop("disabled", false);
  } else {
    $("#download-button").prop("disabled", true);
  }
}

function reviewuse() {
  if (enableDownload()) {
    $("#download-button").prop("disabled", false);
  } else {
    $("#download-button").prop("disabled", true);
  }
}

function checkack() {
  if (enableDownload()) {
    $("#download-button").prop("disabled", false);
  } else {
    $("#download-button").prop("disabled", true);
  }
}


