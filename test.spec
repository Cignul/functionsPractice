test.tests = function () {
    var cubed = test.cubed
    var power = test.power
    var modByX = test.modByx
    var findById = test.findById
    var letterCount = test.letterCount
    var pythagorean = test.pythagorean
    var sumAll = test.sumAll
    var isEqual = test.isEqual
    var inStock = test.inStock
    describe('The Review', function () {
        var users = [{ id: 1, name: 'Jon' }, { id: 2, name: 'Yuli' }, { id: 21, name: 'Peter' }, { id: 17, name: 'St. MaryLou de la playa carmen' }, { id: 51, name: 'Doug' }, { id: 881, name: 'Paul' }, { id: 0, name: 'Jon' }, { id: 999, name: 'Timma' }]

        it('`cubed(3)` returns the correct value', function () {
            assert.isTrue(cubed(3) === 27)
        })
        it('`cubed(4)` returns the correct value', function () {
            assert.isTrue(cubed(4) === 64)
        })
        it('`power(2,4)` returns the correct value', function () {
            assert.isTrue(power(2, 4) === 16)
        })
        it('`modByX([1,2,3],3)` returns the correct values', function () {
            assert.isTrue(modByX([1, 2, 3], 3)[2] === 0)
        })

        it('`findById(17)` returns the correct Person', function () {
            assert.deepEqual(findById(users, 17), { id: 17, name: 'St. MaryLou de la playa carmen' })
        })
        it('`findById(1000)` returns an error object {error: "Sorry that user id could not be found"}', function () {
            assert.deepEqual(findById(users, 1000), { error: 'Sorry that user id could not be found' })
        })

        it('`letterCount("My Dog Skip is Grand", "i")` should return the number of times an i is found"}', function () {
            var x = letterCount("My Dog Skip is Grand", "i")
            assert.isTrue(x == 2)
        })

        it('`letterCount("My Dog Skip is Grand", "g", false)` should return the number of times an G or g is found"}', function () {
            var x = letterCount("My Dog Skip is Grand", "g", false)
            assert.isTrue(x == 2)
        })

        it('`pythagorean(2,4)` should return the value of c^2"', function () {
            var x = pythagorean(2, 4)
            assert.isTrue(x == 20)
        })

        it('`sumAll([1,2,3])` Adds up all the numbers in the array', function () {
            var x = sumAll([1, 2, 3])
            assert.isTrue(x == 6)
        })

        it('`isEqual(1,"1")` should be false', function () {
            var x = isEqual(1, "1")
            assert.isFalse(x)
        })

        it('`inStock(124)` should be false', function () {
            var products = [{
                id: 124,
                name: 'Design Your Own Cage',
                url: 'http://res.cloudinary.com/spartz/image/upload/c_lfill,f_auto,fl_lossy,q_60,w_806/v1/prod/images/e93da6b3583ea782f5b3814305c16960.jpeg',
                quantity: 0,
                price: 1.99
            }]
            var x = inStock(products, 124)
            assert.isFalse(x)
        })

    })
}