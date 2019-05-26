FROM python:3
MAINTAINER John Sanabria - john.sanabria@correounivalle.edu.co
RUN pip install --upgrade oauth2client
RUN pip install gspread PyOpenSSL

