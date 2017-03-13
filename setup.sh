#/bin/sh
set -e

export DATABASE_URL='postgres://admin:bcadminpass123@localhost:5432/venuebooker'

# logging colour functions
bold=$(tput bold)
red=$(tput setaf 1)
normal=$(tput sgr0)

print(){
    echo "${bold}$*${normal}"
}

error(){
    echo "${red}ERROR${normal}: $*" >&2
    exit 1
}

#if which brew &>/dev/null; then
#    print " - brew already installed "
#else
#    print " - installing brew"
#    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
#PATH="$HOME/.linuxbrew/bin:$PATH"
#echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >>~/.bash_profile
#fi

#if which python3 &>/dev/null; then
#    print " - python3 already installed"
#else
#    print " - installing python3"
#    brew install python3
#fi

#if which virtualenv &>/dev/null; then
 #   print " - virtualenv already installed"
#else
  #  print " - installing virtualenv"
 #   pip install virtualenv
#fi

#if which postgres &>/dev/null; then
#    print " - postgres already installed"
#else
#    print " - installing postgres"
#    brew install postgres
#fi

#TODO - Check if virtual environement exists before removal
#print " - removing virtual environment - venuebooker-env"
#rm -rf venuebooker-env

# setting up django environment
#print " - creating new virtual enviroment - venuebooker-env"
#virtualenv -p python3 venuebooker-env
#source venuebooker-env/bin/activate

print " - installing project deps via pip"
#pip install -r requirements.txt

# creating database
#if psql -l | grep venuebooker | wc -l; then
#    print " - dropping existing venuebooker database"
#    dropdb venuebooker
#fi

print " - creating venuebooker database"
#createdb venuebooker

#sudo -su postgres
#USER=$(psql postgres -tAc "SELECT 1 from pg_roles where rolname='admin'")

# creating postgres user
#if [ "$USER" == "1" ]; then
#    print " - postgres admin user already exists"
#else
#    print " - creating postgres admin user "
#    psql -d venuebooker -c "CREATE USER admin WITH PASSWORD 'bcadminpass123'"
#fi

print " - making database migrations"
python manage.py makemigrations web_app

print " - making database migrations"
python manage.py migrate

#print " - populating schema with initial data"
#python manage.py loaddata web_app/fixtures/initial_data.json

print " - running web server"
python manage.py runserver

