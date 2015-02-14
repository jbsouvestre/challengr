import {LayoutView} from 'marionette';

import Nav from './nav';

let Layout = LayoutView.extend({
    template: require('__templates__/layout.hbs'),
    regions: {
        header: 'header',
        aside: 'aside',
        main: 'main',
        modals: '#modals'
    },
    onRender: function(){
        this.header.show(Nav);
    }
});

export default new Layout();