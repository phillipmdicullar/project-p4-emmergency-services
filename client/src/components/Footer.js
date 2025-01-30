const today = new Date()
function Footer(){
    
    return(<>  <div class="text-center p-4">
         <p>© {today.getFullYear()} no Copyright</p>
        <a class="text-reset fw-bold" href=""></a>
      </div>
      </>)
}
export default Footer;