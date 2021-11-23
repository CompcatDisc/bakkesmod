$time = $(Get-Date -UFormat "%d.%m.%Y %R")
$user = $env:USERNAME
$computer = $env:COMPUTERNAME
git add -A
git commit -am "$($time) ⭐️ $($user)-$($computer)" 
git push --set-upstream origin $($gitNameBranch)
