import ili from './assets/ili.gif'

export default function Index() {
    return (
        <div class={'container'}>
            <h1>🚚 Vite-Transporter</h1>
            <p class={'pt-2'}>Image Asset Example</p>
            <p>👇</p>
            <img width={'100'} src={ili} alt={'ili'}/>
            <small>🥞 Vite, SolidJS, TailwindCSS</small>
        </div>
    )
};
