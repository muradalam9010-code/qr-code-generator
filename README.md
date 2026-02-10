# QR Code Generator

A professional QR Code Generator web application built with Python (Flask) backend, SQLite database, and HTML/CSS frontend.

## Features

✨ **Core Features:**
- Generate QR codes from any text or URL
- Download generated QR codes as PNG images
- View complete history of generated QR codes
- Responsive design for mobile and desktop
- Real-time QR code generation

## Tech Stack

**Backend:**
- Python 3.8+
- Flask 2.3.2
- Flask-CORS for cross-origin requests
- Flask-SQLAlchemy for ORM
- qrcode library for QR generation
- SQLite for database

**Frontend:**
- HTML5
- CSS3 (with responsive design)
- JavaScript (Vanilla)
- QRCode.js library for client-side QR display

## Project Structure

```
qr-code-generator/
├── backend/
│   ├── app.py              # Flask application & API endpoints
│   ├── requirements.txt    # Python dependencies
│   └── qr_codes.db        # SQLite database (auto-created)
├── frontend/
│   ├���─ index.html         # Main UI
│   └── style.css          # Styling
├── .gitignore
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```
   
   The backend will start on `http://localhost:5000`

### Frontend Setup

1. **Open the frontend in a browser:**
   - Simply open `frontend/index.html` in your web browser
   - Or serve it with a simple HTTP server:
     ```bash
     cd frontend
     python -m http.server 8000
     # Then visit http://localhost:8000
     ```

## API Endpoints

### 1. Generate QR Code
**POST** `/generate`

**Request:**
```json
{
  "data": "https://example.com"
}
```

**Response:**
```json
{
  "message": "QR Code generated successfully",
  "id": 1
}
```

### 2. Get QR Code History
**GET** `/history`

**Response:**
```json
[
  {
    "id": 1,
    "data": "https://example.com",
    "created_at": "2026-02-10T15:39:06"
  }
]
```

## Usage

1. **Start the backend server:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open the frontend:**
   - Open `frontend/index.html` in your browser

3. **Generate QR Codes:**
   - Enter text or URL in the input field
   - Click "Generate QR Code"
   - View the generated QR code
   - Click "Download QR Code" to save as PNG

4. **View History:**
   - All generated QR codes are listed in the history section
   - Shows the data and timestamp of each QR code

## Dependencies

### Python (Backend)
- Flask==2.3.2
- Flask-CORS==4.0.0
- Flask-SQLAlchemy==3.0.5
- qrcode==7.4.2
- Pillow==10.0.0
- python-dotenv==1.0.0

### Frontend
- QRCode.js (loaded via CDN)

## Database Schema

**QRCodeRecord Table:**
```sql
CREATE TABLE qr_code_record (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Features Explanation

### QR Code Generation
- Uses the `qrcode` Python library to generate QR codes
- Supports any text or URL input
- Generates PNG format images

### Database Storage
- SQLite database stores all generated QR codes
- Tracks the data and creation timestamp
- Lightweight and requires no external server

### Frontend UI
- Clean, modern design with gradient backgrounds
- Responsive layout for all screen sizes
- Real-time QR code display
- Download functionality for generated codes

## Future Enhancements

- [ ] User authentication and accounts
- [ ] Bulk QR code generation
- [ ] Custom QR code styling (colors, logos)
- [ ] QR code analytics and tracking
- [ ] Export history as CSV/PDF
- [ ] Social sharing features
- [ ] Dark mode theme

## Troubleshooting

**Issue: "Cannot GET /generate"**
- Ensure the Flask backend is running on `http://localhost:5000`
- Check CORS is enabled in the backend

**Issue: QR code not displaying**
- Verify QRCode.js library is loaded from CDN
- Check browser console for JavaScript errors
- Ensure valid input is provided

**Issue: Database errors**
- Delete `qr_codes.db` file and restart the backend to reset the database
- Ensure the backend directory has write permissions

## License

This project is open source and available under the MIT License.

## Author

Created as a professional QR Code Generator application.

---

**Happy QR Code Generating! 🎉**