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
        socket = connect(ipaddr, 80)
        println(socket)
end
try
        while true
                test_ip()
        end
catch err
        println(err)
end
