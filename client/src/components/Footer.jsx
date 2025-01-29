import './navbar.css'
function Footer() {
    const year = new Date().getFullYear();
  return (
    <footer className="footer text-center p-4 border-top">
      <p>© {year} All Rights Reserved</p>
    </footer>
  );
}
export default Footer;