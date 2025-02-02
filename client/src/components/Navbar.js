import React from 'react';
import { Navbar, Nav, Container, Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { AiFillAlert } from 'react-icons/ai';
const CustomNavbar = () => {
  const navigate = useNavigate();
  const isLoggedIn = localStorage.getItem('access_token');

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  return (
    <Navbar className="sticky-top" bg="dark" variant="dark" expand="lg">
      <Container>
        {/* <Navbar.Brand as={Link} to="/">Emergency Response</Navbar.Brand> */}
        
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
          <Navbar.Brand as={Link} to="/">
          <AiFillAlert size={30} color='red'/>
          Emergency !
        </Navbar.Brand>
            {/* <Nav.Link as={Link} to="/emergencies">Emergency Posts</Nav.Link> */}
            
            <Nav.Link as={Link} to="/About">About</Nav.Link>
            <Nav.Link as={Link} to="/Contact">Contact</Nav.Link>
            <Nav.Link as={Link} to="/createemergencypost">Create Post </Nav.Link>
            <Nav.Link as={Link} to='/EmergencyPostsTable'>Emergency Posts Table</Nav.Link>
            
          </Nav>
          <Nav>
            {isLoggedIn ? (
              <Button variant="outline-light" onClick={handleLogout}>Logout</Button>
            ) : (
              <>
                <Nav.Link as={Link} to="/login">Login</Nav.Link>
                <Nav.Link as={Link} to="/signup">Signup</Nav.Link>
              </>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;