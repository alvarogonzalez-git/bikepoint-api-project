<div align="center">
  <p>
    <img width="38%" alt="tfl logo" src="https://github.com/user-attachments/assets/4a711b29-8347-4f2f-bbfc-27a0f3932192" />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img width="38%" alt="santander cycles logo" src="https://github.com/user-attachments/assets/564ded8a-68db-4b26-989d-97b9882f1fab" />
  </p>

  <h1>BikePoint Data Pipeline</h1>

  <p>
    <strong>A robust ETL pipeline ingesting data from Transport for London (TfL).</strong>
  </p>
</div>

<hr />

<p>
  This project was developed as part of <strong>The Information Lab's Data Engineering School</strong>. It implements a robust ETL (Extract, Transform, Load) pipeline to ingest real-time data from <a href="https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll">Transport for London's (TfL) Unified API</a> regarding Santander Cycles and store it securely in the cloud.
</p>

<p>
  The pipeline automates the retrieval of bike point data and uploads it to an <strong>AWS S3 bucket</strong> for future analysis or warehousing.
</p>

<h2>🚀 Project Architecture</h2>

<p>The pipeline consists of two main stages:</p>
<ol>
  <li><strong>Extract:</strong> A Python script queries the TfL API, handles connectivity errors with retries, and saves raw data locally.</li>
  <li><strong>Load:</strong> A second script checks for local data, authenticates with AWS, uploads files to an S3 bucket, and cleans up local storage upon success.</li>
</ol>

<h3>Tech Stack</h3>
<ul>
  <li><strong>Language:</strong> Python 3.12</li>
  <li><strong>Libraries:</strong> <code>requests</code>, <code>boto3</code>, <code>python-dotenv</code></li>
  <li><strong>Cloud Services:</strong> AWS S3</li>
  <li><strong>Logging:</strong> Python standard <code>logging</code> module</li>
</ul>

<hr />

<h2>📂 Project Structure</h2>

<pre>
├── logs/                   # Generated automatically: Stores runtime logs
├── data/                   # Generated automatically: Temporary staging for JSON files
├── .env                    # Environment variables (AWS Credentials)
├── bikepoint_api_call.py   # Script 1: Extracts data from TfL API
├── load_bikepoints.py      # Script 2: Uploads data to AWS S3
└── README.md
</pre>

<hr />

<h2>🛠️ Setup & Installation</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/bikepoint-pipeline.git
cd bikepoint-pipeline</code></pre>

<h3>2. Install Dependencies</h3>
<p>Ensure you have Python installed, then install the required packages:</p>
<pre><code>pip install requests boto3 python-dotenv</code></pre>

<h3>3. Configure Environment Variables</h3>
<p>Create a <code>.env</code> file in the root directory to store your AWS credentials securely. This project uses <code>python-dotenv</code> to load these secrets.</p>

<p><strong>File: <code>.env</code></strong></p>
<pre><code>AWS_ACCESS_KEY=your_access_key_here
AWS_SECRET_KEY=your_secret_key_here
AWS_BUCKET_NAME=your_s3_bucket_name</code></pre>

<hr />

<h2>🏃 Usage</h2>

<h3>Phase 1: Extraction</h3>
<p>Run the extraction script to fetch the latest BikePoint data. This will create a timestamped JSON file in the <code>data/</code> directory and log the attempt in <code>logs/</code>.</p>
<pre><code>python bikepoint_api_call.py</code></pre>
<ul>
  <li><strong>Features:</strong> Implements a retry mechanism (3 attempts) for 500-level server errors and logs success/failure with timestamps.</li>
</ul>

<h3>Phase 2: Loading (S3 Upload)</h3>
<p>Run the upload script to move the JSON files to AWS S3.</p>
<pre><code>python load_bikepoints.py</code></pre>
<ul>
  <li><strong>Features:</strong> Scans the <code>data/</code> directory, uploads files to the bucket defined in your <code>.env</code>, and auto-deletes the local file <em>only</em> if the upload is successful.</li>
</ul>

<h2>📄 License</h2>
<p>This project is open source and available under the <a href="LICENSE">MIT License</a>.</p>
