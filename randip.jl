##Network Mapper for Julia lang

using IPNets

##Static Functions
function input(prompt::AbstractString = "")
	print(prompt * " ")
	chomp(readline())
end

function genIP()
  ip = Any[]
  for i in rand(1:255, 4)
    push!(ip, i)
  end
  global ranaddr = join(ip, ".")
end

function tasks()
  print("Host: ", ranaddr, " down on ", mytask, "\n")
  print(err)
  print("\n")
end
##Argument Functions
function NetMask()
  inputIP = input("Enter IP starting range: ")
  mask = "/24"
  ipAddr = IPv4Net("$inputIP$mask")
  i = 1
  while i < length(ipAddr)
    try
      socket = connect(ipAddr[i], 80)
      print("Host: ", ipAddr[i], " up!..\n")
      i = i + 1
      close(socket)
    catch LoadError
      print("Host: ", ipAddr[i], " down..\n")
      i = i + 1
    end
  end
end

function randIP()
  genIP()
  k = 0
  while k != 1
    try
      #socket0
      print("Connecting to ", ranaddr, " on socket0\n")
      socket0 = @async connect(ranaddr, 80)
      #socket1
      genIP()
      print("Connecting to ", ranaddr, " on socket1\n")
      socket1 = @async connect(ranaddr, 80)
      #socket2
      genIP()
      print("Connecting to ", ranaddr, " on socket2\n")
      socket2 = @async connect(ranaddr, 80)
      #socket3
      genIP()
      print("Connecting to ", ranaddr, " on socket3\n")
      socket3 = @async connect(ranaddr, 80)
      sleep(10)
      print("Host: ", ranaddr, " up!..\n")
      genIP()
    catch LoadError
      tasks()
      genIP()
    end
  end
end

try
  if ARGS[1] == "-n"
    NetMask()
  elseif ARGS[1] == "-r"
    randIP()
  else
    print("Usage: -n Netmask -r randip\n")
  end
catch BoundsError
  print("Usage: -n Netmask -r randip\n")
end
