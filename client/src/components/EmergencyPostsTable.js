import React, { useState, useEffect } from 'react';
import { Button, Table, Modal, Form } from 'react-bootstrap';
import api from '../utils/api';

const EmergencyPostsTable = () => {
  const [emergencies, setEmergencies] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedPost, setSelectedPost] = useState({ id: null, location: '', type: '', description: '' });

  useEffect(() => {
    fetchEmergencies();
  }, []);

  const fetchEmergencies = async () => {
    try {
      const response = await api.get('/emergencies');
      setEmergencies(response.data);
    } catch (error) {
      console.error('Error fetching emergencies', error);
    }
  };

  const handleEdit = (post) => {
    setSelectedPost(post);
    setShowModal(true);
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/emergencies/${id}`);
      console.log('Post deleted successfully!');
      fetchEmergencies();
    } catch (error) {
      console.error('Error deleting post', error);
    }
  };

  const handleSave = async () => {
    try {
      if (selectedPost.id !== null) {
        await api.put(`/emergencies/${selectedPost.id}`, selectedPost);
        console.log('Post updated successfully!');
      } else {
        await api.post('/emergencies', selectedPost);
        console.log('Post created successfully!');
      }
      fetchEmergencies();
      setShowModal(false);
    } catch (error) {
      console.error('Error saving post', error);
    }
  };

  const handleModalClose = () => {
    setShowModal(false);
    setSelectedPost({ id: null, location: '', type: '', description: '' });
  };

  return (
    <div className="container mt-4">
      <Button variant="success" onClick={() => setShowModal(true)}>Add New Post</Button>
      <Table striped hover responsive className="mt-4">
        <thead>
          <tr>
            <th>Location</th>
            <th>Type</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {emergencies.map((post) => (
            <tr key={post.id}>
              <td>{post.location}</td>
              <td>{post.type}</td>
              <td>{post.description}</td>
              <td>
                <Button variant="info" size="sm" className="me-2" onClick={() => handleEdit(post)}>
                  Edit
                </Button>
                <Button variant="danger" size="sm" onClick={() => handleDelete(post.id)}>
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      <Modal show={showModal} onHide={handleModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>{selectedPost.id ? 'Edit Emergency Post' : 'Add New Emergency Post'}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3">
              <Form.Label>Location</Form.Label>
              <Form.Control type="text" placeholder="Location" onChange={(e) => setSelectedPost({ ...selectedPost, location: e.target.value })} value={selectedPost.location || ''} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Type</Form.Label>
              <Form.Control type="text" placeholder="Type" onChange={(e) => setSelectedPost({ ...selectedPost, type: e.target.value })} value={selectedPost.type || ''} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Description</Form.Label>
              <Form.Control as="textarea" rows={3} placeholder="Description" onChange={(e) => setSelectedPost({ ...selectedPost, description: e.target.value })} value={selectedPost.description || ''} />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleModalClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSave}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default EmergencyPostsTable;
