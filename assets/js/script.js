// function redirectToGoogle() {
//     window.location.href = "https://www.google.com";
//   }
  
// var googleButton = document.getElementById("google-button");
// googleButton.onclick = redirectToGoogle;



const downloadButton = document.getElementById('download-button');
const selectYear = document.getElementById('select-year');
const selectedModel = document.querySelector( 'input[name="model"]:checked');   


button.addEventListener('click', disableButton);
downloadButton.addEventListener('click', () => {
  const downloadUrl = 'https://storage.cloud.google.com/co2_app/GPP_CTE_ST_NT_ML/COG/gpp_cte_st_nt_ml_2020_cog.tif'; // replace with your signed URL
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute('href', downloadUrl);
  downloadAnchor.setAttribute('target', '_blank');
  downloadAnchor.setAttribute('download', ''); // empty string sets the filename to the original filename
  downloadAnchor.click();
});
