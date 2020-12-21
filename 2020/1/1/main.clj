(defn read-input
  [filename]
  (->> filename
       slurp
       clojure.string/split-lines
       (map #(Integer/parseInt %))))

(defn calculate
  [numbers]
  (for [a numbers
        b numbers
        :when (< a b)
        :when (= 2020 (+ a b))]
    (* a b)))

(defn main
  []
  (let [numbers (read-input "input.txt")]
    (calculate numbers)))

(println (first (main)))