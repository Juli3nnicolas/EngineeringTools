FROM ubuntu:latest

# Set up man utility
# Do not exclude man pages & other documentation
RUN rm /etc/dpkg/dpkg.cfg.d/excludes && \
    # Reinstall all currently installed packages in order to get the man pages back
    apt-get update && \
    dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall && \
    rm -r /var/lib/apt/lists/* && \
    # Install dev packages
    apt-get update && \
    apt-get install -y man vim git tig && \
    # Enable auto completion for git
    echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

WORKDIR /app
