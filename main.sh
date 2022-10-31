if cat /proc/1/cgroup | tail -1 | grep -q "container"; then
  echo "this is linux container, please use a live usb"
else
  full_fs=$(df ~ | tail -1 | awk '{print $1;}')  
  fs=$(basename $full_fs)                       
  if grep -q "$fs" /proc/partitions; then
    echo "You are using regular linux install,  please use a live usb"
  else
    echo "Starting the process"
    python3 ./code.py
  fi
fi