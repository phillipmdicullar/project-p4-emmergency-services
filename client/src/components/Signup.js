import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';
import api from '../utils/api';
import { MDBContainer, MDBCard, MDBCardBody, MDBCardTitle, MDBInput, MDBBtn, MDBIcon } from 'mdb-react-ui-kit';

const Signup = () => {
  const navigate = useNavigate();

  const initialValues = {
    username: '',
    email: '',
    password: '',
  };

  const validationSchema = Yup.object({
    username: Yup.string().required('Username is required'),
    email: Yup.string().email('Invalid email').required('Email is required'),
    password: Yup.string().required('Password is required'),
  });

  const onSubmit = async (values) => {
    try {
      console.log("Sending data:", values); 
      const response = await api.post('/register', values);
      console.log(response.data);
      navigate('/login');
    } catch (error) {
      console.error('Signup failed:', error.response?.data || error.message);
      alert('Signup failed. Please try again.');
    }
  };

  return (
    <MDBContainer className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
      <MDBCard style={{ width: '100%', maxWidth: '400px' }}>
        <MDBCardBody>
          <MDBCardTitle className="text-center mb-4">Signup</MDBCardTitle>

          <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
          >
            <Form>
              <div className="mb-3">
                <label htmlFor="username" className="form-label">Username</label>
                <Field
                  type="text"
                  name="username"
                  className="form-control"
                  id="username"
                  placeholder="Enter your username"
                />
                <ErrorMessage name="username" component="div" className="text-danger" />
              </div>

              <div className="mb-3">
                <label htmlFor="email" className="form-label">Email</label>
                <Field
                  type="email"
                  name="email"
                  className="form-control"
                  id="email"
                  placeholder="Enter your email"
                />
                <ErrorMessage name="email" component="div" className="text-danger" />
              </div>

              <div className="mb-3">
                <label htmlFor="password" className="form-label">Password</label>
                <Field
                  type="password"
                  name="password"
                  className="form-control"
                  id="password"
                  placeholder="Enter your password"
                />
                <ErrorMessage name="password" component="div" className="text-danger" />
              </div>

              <MDBBtn type="submit" color="primary" block>
                Signup <MDBIcon fas icon="user-plus" />
              </MDBBtn>
            </Form>
          </Formik>
        </MDBCardBody>
      </MDBCard>
    </MDBContainer>
  );
};

export default Signup;
