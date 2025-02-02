import './home.css';
import { AiFillMedicineBox } from "react-icons/ai";
import { FaHeartbeat, FaAmbulance, FaPhone } from "react-icons/fa";
import { Fade, Slide } from "react-awesome-reveal";

function Home() {
  return (
    <div className="home-container bg-light text-dark">
      <div className="container py-5">
        <div className="row align-items-center">
          {/* Left Section: Emergency Message */}
          <div className="col-lg-6 text-center text-lg-start">
            <div className="message-box animate__animated animate__fadeInLeft">
              <Slide>
              <h1 className="display-5 fw-bold text-danger">
                Stay Alert, Stay Safe
              </h1>
              </Slide>
              <Fade delay={1e3} cascade damping={1e-1}>
              <p className="fs-5 mt-3">
                "Surviving is winning, Franklin. <AiFillMedicineBox size={30} color='black'/>
                <br />
                Everything else is bullshit.
                <br />
                Whatever it takes, kid, survive."
              </p>
              </Fade>
              <Slide>
              <p className="text-muted">Your safety is our priority.</p>
              </Slide>
            </div>

            {/* Emergency Aid Icons */}
            <div className="d-flex justify-content-center justify-content-lg-start gap-3 mt-4">
              <img
                src="aid.png"
                alt="Aid Icon 1"
                className="aid-icon animate__animated animate__zoomIn"
                data-tip="Emergency Aid"
              />
              <img
                src="aid.png"
                alt="Aid Icon 2"
                className="aid-icon animate__animated animate__zoomIn"
                data-tip="Medical Assistance"
              />
              <FaHeartbeat size={30} color="red" data-tip="Heartbeat Monitoring" />
              <FaAmbulance size={30} color="blue" data-tip="Call Ambulance" />
              <FaPhone size={30} color="green" data-tip="Emergency Contact" />
              {/* <ReactTooltip place="top" type="dark" effect="solid" /> */}
            </div>
          </div>

          {/* Right Section: Logo */}
          <div className="col-lg-5 text-center">
            <img
              src="./new1.png"
              alt="My Logo"
              className="logo-img animate__animated animate__bounceIn"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
