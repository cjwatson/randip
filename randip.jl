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

##Argument Functions
function NetMask()
  inputIP = input("Enter IP starting range: ")
  mask = "/24"
  ipAddr = IPv4Net(string(inputIP, mask))
  i = 1
  while i < length(ipAddr)
    try
      connect(ipAddr[i], 80)
      print("Host: ", ipAddr[i], " up!..\n")
      i = i + 1
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
      connect(ranaddr, 80)
      print("Host: ", ranaddr, " up!..\n")
    catch LoadError
      print("Host: ", ranaddr, " down..\n")
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
