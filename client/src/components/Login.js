import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';
import api from '../utils/api';
import { MDBContainer, MDBCard, MDBCardBody, MDBCardTitle, MDBInput, MDBBtn, MDBIcon } from 'mdb-react-ui-kit';

const Login = () => {
  const navigate = useNavigate();

  const initialValues = {
    username: '',
    password: '',
  };

  const validationSchema = Yup.object({
    username: Yup.string().required('Username is required'),
    password: Yup.string().required('Password is required'),
  });

  const onSubmit = async (values) => {
    try {
      const response = await api.post('/login', values);
      localStorage.setItem('access_token', response.data.access_token);
      navigate('/');
    } catch (error) {
      alert('Login failed. Please check your credentials.');
    }
  };

  return (
    <MDBContainer className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
      <MDBCard style={{ width: '100%', maxWidth: '400px' }}>
        <MDBCardBody>
          <MDBCardTitle className="text-center mb-4">Login</MDBCardTitle>

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
                Login <MDBIcon fas icon="sign-in-alt" />
              </MDBBtn>
            </Form>
          </Formik>
        </MDBCardBody>
      </MDBCard>
    </MDBContainer>
  );
};

export default Login;
