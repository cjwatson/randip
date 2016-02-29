function gen_ip()
        ip = Any[]
        for i in rand(1:255, 4)
                push!(ip, i)
        end
        global ipaddr = join(ip, ".")
end

function test_ip()
        gen_ip()
        println("Testing IP: ", ipaddr)
        global socket = connect(ipaddr, 80)
end

function timer()
        sleep(5)
        close(socket)
end

try
        while true
                @async test_ip()
                @async timer()
                timer()
        end
catch err
        println("Simple Error:\n", err, "\n")
        println("Detailed Error: ", error(), "\n")
        println("Bactrace: ", backtrace())
        exit()
end
