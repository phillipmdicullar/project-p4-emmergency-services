import React from "react";
import "./About.css"; 
import { Fade, Slide } from "react-awesome-reveal";
const About = () => {
  return (
    <section id="about" className="about-section py-5 bg-light">
      <div className="container">
        <Slide>
        <div className="row text-center">
          <div className="col-lg-6 mx-auto">
            <h2 className="display-4 mb-4 text-primary">About Our Emergency Alert System</h2>
            <p className="lead">
              Our mission is simple: ensure that help is always within reach in times of need. Whether it's a medical emergency, a natural disaster, or any other critical situation, we are here to help you connect with the right responders, fast.
            </p>
          </div>
        </div>
        </Slide>
        <div className="row mt-5">
          <div className="col-md-4">
            <div className="card border-0 shadow-lg">
              <div className="card-body text-center">
                <i className="fas fa-heartbeat fa-3x mb-3 text-danger"></i>
                <h4 className="card-title text-danger">Medical Assistance</h4>
                <p className="card-text">
                  Our system connects you to medical responders for emergencies like accidents, heart attacks, and more.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card border-0 shadow-lg">
              <div className="card-body text-center">
                <i className="fas fa-fire-extinguisher fa-3x mb-3 text-warning"></i>
                <h4 className="card-title">Fire Response</h4>
                <p className="card-text">
                  In case of fire, we immediately notify the nearest fire department and keep you informed of their arrival.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card border-0 shadow-lg">
              <div className="card-body text-center">
                <i className="fas fa-water fa-3x mb-3 text-info"></i>
                <h4 className="card-title">Flood Support</h4>
                <p className="card-text">
                  Our system helps you connect with flood relief teams, providing immediate guidance and resources.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
