// function redirectToGoogle() {
//     window.location.href = "https://www.google.com";
//   }
  
// var googleButton = document.getElementById("google-button");
// googleButton.onclick = redirectToGoogle;



const downloadButton = document.getElementById('download-button');
const selectYear = document.getElementById('select-year');
const selectedModel = document.querySelector( 'input[name="model"]:checked');   


//downloadButton.addEventListener('click', disableButton);
downloadButton.addEventListener('click', () => {

  //Cedar collection
  var downloadUrl = 'https://storage.cloud.google.com/co2_app/MODEL/COG/gpp_cte_st_nt_YEAR_cog.tif?authuser=0'
 
  var selectedYear = $("#select-year").val();
  var selectedModel = $('input[name="model"]:checked').val();

  downloadUrl = downloadUrl.replace("MODEL", selectedModel);
  downloadUrl = downloadUrl.replace("YEAR", selectedYear);

  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute('href', downloadUrl);
  //downloadAnchor.setAttribute('target', '_blank');
  downloadAnchor.setAttribute('download', ''); // empty string sets the filename to the original filename
  downloadAnchor.click();
});

    // Check the radio button value.
    function modelselect(model) {
      var selectedYear = $("#select-year").val();
      if (selectedYear != "" && model != "") {
        $("#download-button").prop("disabled", false);
      } else {
        $("#download-button").prop("disabled", true);
      }
    }

    function selectyear(year) {
      var selectedYear = $("#select-year").val();
      if (selectedYear != "" && year != "") {
        $("#download-button").prop("disabled", false);
      } else {
        $("#download-button").prop("disabled", true);
      }
    }
