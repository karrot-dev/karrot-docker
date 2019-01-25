#!/bin/bash

# nice colors for ls command

export LS_OPTIONS='--color=auto'
eval "$(dircolors)"
alias ls='ls $LS_OPTIONS'

# define a color for PS1 use

function color() {
  echo "\[$(tput setaf $1)\]"
}

# To find more nice colors
# see https://unix.stackexchange.com/questions/269077/tput-setaf-color-table-how-to-determine-color-codes/269085#269085

reset="\[$(tput sgr0)\]"
white=$(color 15)

karrot=$(color 214)
frontend=$(color 227)
backend=$(color 57)

if [[ "${NAME:-}" = "frontend" ]]; then
  name_color="${frontend}"
else
  name_color="${backend}"
fi

PS1="${karrot}karrot${white}/${name_color}${NAME:-unknown}${white}▶ ${reset}"

# if we're in the backend we want to activate the virtualenv

[[ -f env/bin/activate ]] && source env/bin/activate
