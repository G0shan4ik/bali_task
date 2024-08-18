var a = new Array()
document.querySelectorAll('[data-testid]').forEach(
    el => {a.push(el)}
)
var res = a.filter(
    el => el
        .getAttribute('data-testid')
        .match(/listing-card-\d*$/g))
    .map(el => {
        let a = el.querySelector('div>a:nth-child(2)')
        let id = el.getAttribute('data-testid').replace('listing-card-', '')
        let img_link = a.querySelector('img').src.replace('_progressive_thumbnail', '')
        let title = a.querySelector('img').title
        let price = a.querySelector('p[title]').title.replace(
            'PHP ', ''
        ).replace(',', '').trim()
        //document.querySelector("#main > div.D_Gz > div > section.D_GL > div.D_GQ > div > div > div:nth-child(1) > div:nth-child(1) > div > div.D_nv.M_kq > a:nth-child(2) > div.D_nR.M_kM > p")
        let url = `https://www.carousell.ph/p/${id}`
        return {
            unique_id: Number(id),
            image: img_link,
            name: title,
            price: Number(price),
            url: url
        }
    })
return res;
