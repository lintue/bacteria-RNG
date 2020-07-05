/**
 * Bacteria RNG, 2020.
 */

import '../style/main.scss'

import { a, b, c, d, e, f, g, h, i, j, k, l, m, n, o } from './Media'
import { z } from './Media'

import { Difference } from './components/Hashing'

let $ = require('jquery')

/**
 * Containers.
 */

 if (process.env.NODE_ENV == 'production') {
   $('#loader').fadeOut(3000, function() {
     $(this).remove()
   })
 }

const container = document.createElement('div')
container.id = 'container'
document.body.appendChild(container)

const frame = document.createElement('div')
frame.id = 'frame'
container.appendChild(frame)

const imageBox = document.createElement('div')
const image = document.createElement('img')
imageBox.id = 'image'
frame.appendChild(imageBox)
imageBox.appendChild(image)

const hashing = document.createElement('div')
hashing.id = 'hashing'
frame.appendChild(hashing)

const number = document.createElement('div')
number.id = 'number'
frame.appendChild(number)


/**
 * Image sequence.
 */

const images = [
  a, b, c,
  d, e, f,
  g, h, i,
  j, k, l,
  m, n, o
]

sequencer()

function sequencer() {

  let i = 0
  let hash = z.split('\n')

  window.setInterval(function() {

    image.src = images[i]

    $('#number').fadeIn(50)

    let shuffled = hash[0] + hash[1].split('').sort(function(){ return 0.5 - Math.random() }).join('')
    $('#hashing').text(shuffled)

    $('#number').text(Math.floor(Math.random() * 100))
    $('#number').delay(450).fadeOut(900)

    i = (i + 1) % images.length

  }, 1500)

}
