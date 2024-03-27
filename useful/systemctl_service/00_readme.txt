# create .service file

& vim zondcom_interlayer.service

[Unit]
Description=QMI interlayer for ASTCv2
After=astcv2.service
StartLimitIntervalSec=5
Requires=astcv2.service

[Service]
Type=simple
ExecStart=/usr/bin/python3.11 astcv1MD_to_zondcom_interlayer.py
User=root
RuntimeDirectory=/var/lad/astc2/utils
WorkingDirectory=/var/lad/astc2/utils
PrivateTmp=false
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target

# start service
& systemctl start zondcom_interlayer.service
