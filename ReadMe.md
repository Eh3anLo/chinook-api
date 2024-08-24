### **Create a REST API for Managing the Chinook Database**

- [x]  **Task:** Build RESTful endpoints for CRUD operations on all tables in the Chinook database (e.g., `Artist`, `Album`, `Track`, etc.).
- [x]  **Challenge:** Implement serializers, viewsets, and URL routing. Make sure to handle foreign key relationships correctly.

### **Implement Search Functionality**

- [ ]  **Task:** Create an API endpoint to search for tracks by name, artist, album, or genre.
- [ ]  **Challenge:** Optimize queries to handle large datasets efficiently, and return results with pagination.

### **Bulk Import of Track Data**

- [x]  **Task:** Develop a feature that allows bulk uploading of track data via CSV or JSON.
- [x]  **Challenge:** Use Celery to handle the bulk import asynchronously, ensuring that large files are processed in the background without blocking the main thread.