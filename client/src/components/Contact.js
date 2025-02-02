import { DotLottieReact } from '@lottiefiles/dotlottie-react';
import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import "bootstrap/dist/css/bootstrap.min.css";

const Contact = () => {
  return (
    <div className="container mt-5">
            <div className="h-screen">
      <DotLottieReact
      src="https://lottie.host/126d7d82-97e1-48f8-b230-ee9bbe3e46a7/gAQA5cgG0d.lottie"
      loop
      autoplay
    />
      </div>
      <div className="card shadow-lg p-4">
        <h2 className="text-center mb-4">Contact Us</h2>
        <Formik
          initialValues={{ name: "", email: "", message: "" }}
          validationSchema={Yup.object({
            name: Yup.string()
              .min(2, "Too Short!")
              .max(50, "Too Long!")
              .required("Name is required"),
            email: Yup.string()
              .email("Invalid email address")
              .required("Email is required"),
            message: Yup.string()
              .min(10, "Message too short")
              .required("Message is required"),
          })}
          onSubmit={(values, { setSubmitting, resetForm }) => {
            console.log("Form submitted", values);
            alert("Message sent successfully!");
            setSubmitting(false);
            resetForm();
          }}
        >
          {({ isSubmitting }) => (
            <Form>
            <div className='design'>
              <div className="mb-3">
                <label className="form-label">Name</label>
                <Field
                  type="text"
                  name="name"
                  className="form-control"
                  placeholder="Enter your name"
                />
                <ErrorMessage name="name" component="div" className="text-danger" />
              </div>

              <div className="mb-3">
                <label className="form-label">Email</label>
                <Field
                  type="email"
                  name="email"
                  className="form-control"
                  placeholder="Enter your email"
                />
                <ErrorMessage name="email" component="div" className="text-danger" />
              </div>

              <div className="mb-3">
                <label className="form-label">Message</label>
                <Field
                  as="textarea"
                  name="message"
                  className="form-control"
                  rows="4"
                  placeholder="Your message here..."
                />
                <ErrorMessage name="message" component="div" className="text-danger" />
              </div>

              <button type="submit" className="btn btn-primary w-100" disabled={isSubmitting}>
                {isSubmitting ? "Sending..." : "Send Message"}
              </button>
            </div>
            </Form>
          )}
        </Formik>
      
      </div>
 
    </div>
  );
};

export default Contact;
