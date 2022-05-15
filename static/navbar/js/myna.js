const search = document.getElementById('sinp')

search.addEventListener('keypress',  (event)=>
{
    if(event.key ==='Enter'){
         console.log(String(search.value).toLowerCase())
        open('auth/login')
    }
})