function main()
    local horizontal = 0
    local depth = 0
    local aim = 0
    local content = readlines("input.txt")
    for line in content
        direction, unit = split(line, " ")
        unit = parse.(Int, unit)
        if direction == "forward"
            horizontal += unit
            depth += aim * unit
        elseif direction == "up"
            aim -= unit
        elseif direction == "down"
            aim += unit
        end
    end
    println(horizontal * depth)
end

main()