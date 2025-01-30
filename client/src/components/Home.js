import './home.css';

function Home() {
  return (
    <div className="home-container bg-light text-dark">
      <div className="container py-5">
        <div className="row align-items-center">
          {/* Left Section: Emergency Message */}
          <div className="col-lg-6 text-center text-lg-start">
            <div className="message-box animate__animated animate__fadeInLeft">
              <h1 className="display-5 fw-bold text-danger">
                Stay Alert, Stay Safe
              </h1>
              <p className="fs-5 mt-3">
                "Surviving is winning, Franklin.<br />
                Everything else is bullshit.<br />
                Whatever it takes, kid, survive."
              </p>
              <p className="text-muted">Your safety is our priority.</p>
            </div>

            {/* Emergency Aid Icons */}
            <div className="d-flex justify-content-center justify-content-lg-start gap-3 mt-4">
              <img
                src="aid.png"
                alt="Aid Icon 1"
                className="aid-icon animate__animated animate__zoomIn"
              />
              <img
                src="aid.png"
                alt="Aid Icon 2"
                className="aid-icon animate__animated animate__zoomIn"
              />
            </div>
          </div>

          {/* Right Section: Logo */}
          <div className="col-lg-6 text-center">
            <img
              src="./logo.png"
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
