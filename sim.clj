(ns sim)

(def building-supplies
  {:nails {:metal 2
           :time 4}
   :planks {:wood 2
            :time 24}
   :bricks {:minerals 2
            :time 16}
   :cement {:minerals 2
            :chemicals 1
            :time 40}
   :glue {:plastic 1
          :chemicals 2
          :time 48}
   :paint {:metal 2
           :minerals 1
           :chemicals 2
           :time 48}})

(def hardware
  {:hammer  {:metal 1
             :wood 1
             :time 11.2}
   :measuring-tape {:metal 1
                    :plastic 1
                    :time 16}
   :shovel {:metal 1
            :wood 1
            :plastic 1
            :time 24}
   :cooking-utensils {:metal 2
                      :wood 2
                      :plastic 2
                      :time 36}
   :ladder {:metal 2
            :planks 2
            :time 48}
   :drill {:metal 2
           :plastic 2
           :electrical-components 1
           :time 96}})

(def fashion
  {:cap {:textiles 2
         :measuring-tape 1
         :metal 1
         :plastic 1
         :time 51}
   :shoes {:textiles 2
           :plastic 2
           :glue 1
           :chemicals 2
           :time 63}
   :watch {:plastic 2
           :glass 1
           :chemicals 1
           :time 76}
   :business-suits {:textiles 3
                    :measuring-tape 1
                    :metal 1
                    :plastic 1
                    :glue 1
                    :plastic 1
                    :chemicals 2
                    :time 178}
   :backpack {:textiles 2
              :plastic 2
              :measuring-tape 1
              :metal 1
              :plastic 1
              :time 127}})

(def furniture
  {:chairs {:wood 2
            :nails 1
            :hammer 1
            :metal 1
            :wood 1
            :time 16}
   :tables {:planks 1
            :wood 2
            :nails 2
            :hammer 1
            :metal 1
            :wood 1
            :time 24}
   :home-textiles {:textiles 2
                   :measuring-tape 1
                   :metal 1
                   :plastic 1
                   :time 60}
   :cupboard {:planks 2
              :wood 2
              :glass 2
              :paint 1
              :metal 2
              :minerals 1
              :chemicals 2
              :time 36}
   :couch {:textiles 3
           :drill 1
           :metal 2
           :plastic 2
           :electrical-components 1
           :glue 1
           :plastic 1
           :chemicals 2
           :time 120}})

(def farmers-market
  {:beef {:animal-feed 3
          :time 120}
   :vegetables {:seeds 2
                :time 16}
   :flour-bag {:seeds 2
               :textiles 2
               :time 24}
   :fruit-and-berries {:seeds 4
                       :tree-saplings 1
                       :shovel 1
                       :metal 1
                       :wood 1
                       :plastic 1
                       :time 72}
   :cream {:animal-feed 1
           :time 60}
   :corn {:minerals 1
          :seeds 4
          :time 48}
   :cheese {:animal-feed 2
            :time 84}})

(def gardening-supplies
  {:grass {:seeds 1
           :shovel 1
           :metal 1
           :wood 1
           :plastic 1
           :time 24}
   :tree-saplings {:seeds 2
                   :shovel 1
                   :metal 1
                   :wood 1
                   :plastic 1
                   :time 72}
   :garden-furniture {:planks 2
                      :wood 2
                      :plastic 2
                      :textiles 2
                      :time 108}
   :fire-pit {:bricks 2
              :minerals 2
              :shovel 1
              :metal 1
              :wood 1
              :plastic 1
              :cement 2
              :time 202}
   :lawn-mower {:metal 5
                :paint 1
                :minerals 1
                :chemicals 2
                :electrical-components 1
                :time 96}
   :garden-gnomes {:cement 2
                   :glue 1
                   :plastic 1
                   :chemicals 2
                   :time 72}})

(def donut-shop
  {:donuts {:flour-bag 1
            :seeds 2
            :textiles 2
            :sugar-and-spices 1
            :time 38.25}
   :green-smoothie {:vegetables 1
                    :seeds 2
                    :fruit-and-berries 1
                    :seeds 4
:tree-saplings 1
:shovel 1
:metal 1
:wood 1
:plastic 1
                    :time 25.5}
   :bread-roll {:flour-bag 2
                :seeds 2
                :textiles 2
                :cream 1
                :animal-feed 1
                :time 51}
   :cherry-cheesecake {:flour-bag 1
                       :seeds 2
                       :textiles 2
                       :fruit-and-berries 1
                       :tree-saplings 1
:shovel 1
:metal 1
:wood 1
:plastic 1
                       :cheese 1
                       :animal-feed 2
                       :time 76}
   :frozen-yogurt {:fruit-and-berries 1
                   :tree-saplings 1
:shovel 1
:metal 1
:wood 1
:plastic 1
                   :cream 1
                   :animal-feed 1
                   :sugar-and-spices 1
                   :time 204}
   :coffee {:cream 1
            :animal-feed 1
            :seeds 2
            :sugar-and-spices 1
            :time 51}})

(def fast-food
  {:ice-cream-sandwich {:bread-roll 1
                        :cream 2
:animal-feed 2
:flour-bag 2
:seeds 2
:textiles 2
                        :cream 2
                        :animal-feed 2
                        :flour-bag 2
:seeds 2
:textiles 2
                        :time 12.6}
   :pizza {:flour-bag 1
           :seeds 2
:textiles 2
           :cheese 1
           :beef 1
           :animal-feed 5
           :time 21.6}
   :burgers {:beef 1
             :bread-roll 1
             :cream 4
:animal-feed 4
:flour-bag 2
:seeds 2
:textiles 2
             :bbq-grill 1
             :metal 5
:cooking-utensils 1
:wood 2
:plastic 2
             :time 31.5}
   :cheese-fries {:vegetables 1
                  :seeds 2
                  :cheese 1
                  :animal-feed 2
                  :time 18}
   :lemonade-bottle {:fruit-and-berries 1
                     :tree-saplings 1
:shovel 1
:metal 1
:wood 1
:plastic 1
                     :glass 2
                     :sugar-and-spices 2
                     :time 54}
   :popcorn {:microwave-oven 1
             :metal 4
:glass 1
:electrical-components 1
             :corn 2
             :minerals 1
:seeds 4
             :time 27}})

(def home-appliances
  {:bbq-grill {:metal 5
               :cooking-utensils 1
:wood 2
:plastic 2
               :time 148}
   :refrigerator {:plastic 2
                  :chemicals 2
                  :electrical-components 2
                  :time 189}
   :lighting-system {:chemicals 1
                     :electrical-components 1
                     :glass 1
                     :time 94}
   :tv {:plastic 2
        :glass 2
        :electrical-components 2
        :time 135}
   :microwave-oven {:metal 4
                    :glass 1
                    :electrical-components 1
                    :time 108}})

(def stores 
  [building-supplies hardware fashion furniture farmers-market gardening-supplies donut-shop fast-food home-appliances])

(mapcat keys stores)

(defn item [k]
  (-> (some k stores)
      (assoc k 1)
      (dissoc :time)))

(item :beef)

(def prod
  [:bread-roll :shovel :shovel :shovel :popcorn 
   :business-suits
   :bricks :bricks :bricks :bricks :tv :flour-bag :flour-bag
   :burgers :burgers :burgers :garden-furniture :garden-furniture :garden-furniture :beef
   :paint :paint :paint :paint :tree-saplings :tree-saplings :tree-saplings
   :burgers :burgers :cherry-cheesecake :cherry-cheesecake :cherry-cheesecake
   :cheese-fries :cheese-fries
   :shoes :shoes :shoes
   :ice-cream-sandwich :ice-cream-sandwich :ice-cream-sandwich :watch :watch :watch])

(defn items [l]
  (mapcat #(seq (item %)) l))

(items prod)

(defn n [item l]
  (reduce + (map last
                 (filter #(= item (first %))
                         (items l)))))

(def materials [:metal :wood :plastic :seeds :minerals :chemicals :textiles :sugar-and-spices :glass :animal-feed :electrical-components])

(reverse (sort-by #(first (vals %))
                  (for [m materials]
                    {m (n m prod)})))

(defn parts [l]
  (for [m l]
    {m (n m prod)}))

(reverse (sort-by #(first (vals %))
                  (remove #(zero? (first (vals %)))
                          (parts (mapcat keys stores)))))

