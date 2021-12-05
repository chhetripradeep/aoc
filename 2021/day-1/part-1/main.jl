function main()
    local result = 0
    local content = readlines("input.txt")
    local lines = parse.(Int, content)
    for i in 2:length(lines)
        if lines[i] > lines[i-1]
            result += 1
        end
    end
    println(result)
end

main()