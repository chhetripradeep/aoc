(defn read-input
  [filename]
  (->> filename
       slurp
       clojure.string/split-lines))

(defn filter-direction
  [item]
  (first (clojure.string/split item #" ")))

(defn filter-unit
  [item]
  (Integer/parseInt (last (clojure.string/split item #" "))))

(defn calculate
  [input]
  (let [horizontal (atom 0)
        depth (atom 0)
        aim (atom 0)]
    (doseq [item input]
      (let [direction (filter-direction item)
            unit (filter-unit item)]
        (cond
          (= direction "up") (swap! aim - unit)
          (= direction "down") (swap! aim + unit)
          (= direction "forward") (do
                                    (swap! horizontal + unit)
                                    (swap! depth + (* @aim unit))))))
    (* @depth @horizontal)))

(defn main
  []
  (let [input (->> "input.txt"
                   read-input)]
    (->> input
         calculate)))

(print (main))
