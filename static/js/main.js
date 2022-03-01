// Get search form and page links
let search_form = document.getElementById('search_form')
let page_links = document.getElementsByClassName('page-link')

// Ensure search form exist 
if (search_form){
  for (let i=0; page_links.length > i; i++){
    page_links[i].addEventListener('click', function(e){
      e.preventDefault()
      // Get the data attribute 
      let page = this.dataset.page
      // Add hidden search input to form
      search_form.innerHTML += `<input value=${page} name="page" hidden />`
      // Submit the form
      search_form.submit()
    })
  }
}
