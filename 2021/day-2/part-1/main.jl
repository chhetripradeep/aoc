function main()
    local horizontal = 0
    local depth = 0
    local content = readlines("input.txt")
    for line in content
        direction, unit = split(line, " ")
        unit = parse.(Int, unit)
        if direction == "forward"
            horizontal += unit
        elseif direction == "up"
            depth -= unit
        elseif direction == "down"
            depth += unit
        end
    end
    println(horizontal * depth)
end

main()