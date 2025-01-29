import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Layout";
import Home from "../Pages/Home";
import EmergencyPosts from "../Pages/EmergencyPosts";
import UserProfile from "../Pages/UserProfile";
import Login from "../Pages/Login";
import Register from "../Pages/Register";
import NotFound from "../Pages/NotFound";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/emergencies" element={<EmergencyPosts />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
