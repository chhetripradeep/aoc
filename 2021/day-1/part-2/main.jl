function main()
    local result = 0
    local content = readlines("input.txt")
    local lines = parse.(Int, content)
    for i in 4:length(lines)
        local lower_sum = sum(lines[i-3:i-1])
        local upper_sum = sum(lines[i-2:i])
        if upper_sum > lower_sum
            result += 1
        end
    end
    println(result)
end

main()