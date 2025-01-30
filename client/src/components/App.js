import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import React from "react";
import CustomNavbar from '../components/Navbar'
import Login from '../components/Login'
import Signup from '../components/Signup'
import ProtectedRoute from '../components/ProtectedRoute'
import About from '../components/About'
import EmergencyPosts from '../components/EmergencyPosts'
import Home from '../components/Home'
import Footer from '../components/Footer'
// import CreateEmergencyPost from '../components/CreateEmergencyPost'
// import EmergencyPosts from '../components/emergencies'
import NotFound from '../components/NotFound'

import EmergencyPostsTable from "./EmergencyPostsTable";
function App() {
  return (
    <Router>
      <CustomNavbar />
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="*" element={<NotFound />} />
      <Route element={<ProtectedRoute />}>
          <Route path="/emergencies" element={<EmergencyPosts />} />
          <Route path="/createemergencypost" element={<EmergencyPostsTable />} />
      </Route>
      </Routes>
      <About />
    <Footer />
    </Router>
  );
}

export default App;
