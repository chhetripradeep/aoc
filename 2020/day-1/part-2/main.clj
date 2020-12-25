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
        c numbers
        :when (and (< a b) (< b c))
        :when (= 2020 (+ a b c))]
    (* a b c)))

(defn main
  []
  (let [numbers (read-input "input.txt")]
    (calculate numbers)))

(println (first (main)))