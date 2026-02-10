from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import qrcode
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_codes.db'
CORS(app)

db = SQLAlchemy(app)

class QRCodeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<QRCodeRecord {self.data}>'

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Generate QR code
    qr = qrcode.make(data)
    img = io.BytesIO()
    qr.save(img, format='PNG')
    img.seek(0)
    
    # Save to database
    record = QRCodeRecord(data=data)
    db.create_all()
    db.session.add(record)
    db.session.commit()
    
    return jsonify({'message': 'QR Code generated successfully', 'id': record.id}), 200

@app.route('/history', methods=['GET'])
def history():
    records = QRCodeRecord.query.all()
    return jsonify([{'id': r.id, 'data': r.data, 'created_at': r.created_at} for r in records]), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)