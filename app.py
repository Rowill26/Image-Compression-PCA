from flask import Flask, render_template, request, send_file, url_for
import os
from werkzeug.utils import secure_filename
from main import compress_image_pca

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['COMPRESSED_FOLDER'] = 'static/compressed/'

# Pastikan folder tersedia saat program dijalankan
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['COMPRESSED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'Tidak ada file yang diunggah', 400
        
        file = request.files['image']
        if file.filename == '':
            return 'File belum dipilih', 400
        
        n_components = int(request.form.get('n_components', 50))
        
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        output_filename = f"compressed_{filename}"
        output_path = os.path.join(app.config['COMPRESSED_FOLDER'], output_filename)
        
        runtime, comp_pct = compress_image_pca(input_path, output_path, n_components)
        
        return render_template('index.html', 
                               input_img=url_for('static', filename=f'uploads/{filename}'),
                               output_img=url_for('static', filename=f'compressed/{output_filename}'),
                               runtime=round(runtime, 3),
                               comp_pct=round(comp_pct, 2),
                               download_url=url_for('download_file', filename=output_filename))   
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.config['COMPRESSED_FOLDER'], filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)