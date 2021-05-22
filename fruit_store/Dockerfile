FROM ubuntu:18.04

# Get Miniconda
COPY Miniconda3-latest-Linux-x86_64.sh /miniconda.sh
ENV PATH="/root/miniconda/bin:${PATH}"
RUN chmod +x /miniconda.sh && /miniconda.sh -b -p /root/miniconda && \
    # pip  install numpy==1.17.0 && \
    rm /miniconda.sh

# Install pip and install tools
RUN apt update && pip install --upgrade pip && \
    apt install -y nano=2.9.3-2 \
    openssh-server \
    curl

# RUN apt-get update && apt-get install -y mysql-server mysql-client

# Add SSH server
RUN mkdir /var/run/sshd && \
    sed -r -i 's/^#?PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config && \
    mkdir /root/.ssh && chmod 700 /root/.ssh && \
    touch /root/.ssh/authorized_keys && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    # ENV variable is cleaned, so add again here for safekeeping
    echo "export PATH=/root/miniconda/bin:${PATH}" >> /etc/profile

# # Copy ssh-key for cloning git
# COPY ./cache/id_rsa /
# COPY ./cache/id_rsa.pub /
# COPY ./cache/known_hosts /
# COPY ./cache/authorized_keys /
# RUN mv id_rsa ~/.ssh/id_rsa && \
#     mv id_rsa.pub ~/.ssh/id_rsa.pub && \
#     mv known_hosts ~/.ssh/known_hosts && \
#     mv authorized_keys ~/.ssh/authorized_keys && \
#     cd ~/.ssh/ && \
#     chmod 600 id_rsa && \
#     chmod 600 id_rsa.pub

ADD . /home/fruit_store

WORKDIR /home/fruit_store

RUN rm Miniconda3-latest-Linux-x86_64.sh && rm -rf cache

RUN pip install -r requirements.txt

# Install mongodb
RUN apt-get update && apt-get install -y mongodb && \
    mongod --repair --dbpath /var/lib/mongodb && \
    mongod --fork --logpath /var/lib/mongodb/mongodb.log --dbpath /var/lib/mongodb

CMD mongod --repair --dbpath /var/lib/mongodb && \
    mongod --fork --logpath /var/lib/mongodb/mongodb.log --dbpath /var/lib/mongodb && \
    /usr/sbin/sshd -D 


