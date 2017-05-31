# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Setup Django environment variables
export DJANGO_SETTINGS_MODULE=djproject.settings
export PYTHONPATH=~/DJANGOX/djproject/

# Set PATH to include netmiko-tools
export PATH=$PATH:/home/nlinkov/netmiko_tools/netmiko_tools

# Login to the applied python virtualenv
source /home/nlinkov/applied_python/bin/activate

# Add host entries
function resolve {
        hostfile=~/.hosts
        if [[ -f "$hostfile" ]]; then
                for arg in $(seq 1 $#); do
                        if [[ "${!arg:0:1}" != "-" ]]; then
                                ip=$(sed -n -e "/^\s*\(\#.*\|\)$/d" -e "/\<${!arg}\>/{s;^\s*\(\S*\)\s*.*$;\1;p;q}" "$hostfile")
                                if [[ -n "$ip" ]]; then
                                        command "${FUNCNAME[1]}" "${@:1:$(($arg-1))}" "$ip" "${@:$(($arg+1)):$#}"
                                        return
                                fi
                        fi
                done
        fi
        command "${FUNCNAME[1]}" "$@"
}

function ping {
        resolve "$@"
}

function traceroute {
        resolve "$@"
}

function ssh {
        resolve "$@"
}
