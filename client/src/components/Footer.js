import { AiFillAlert } from "react-icons/ai";
const today = new Date();
function Footer() {
  return (
    <>
      <div className="bg-theme p-10 font-mont text-center">
      </div>
      <div className="flex"></div>
      <div className="bg-theme p-4 text-center">
        <p>© {today.getFullYear()} no Copyright</p>
      </div>
    </>
  );
}
export default Footer;
